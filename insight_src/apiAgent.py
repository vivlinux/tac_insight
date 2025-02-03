import os
import yaml
from langchain_community.agent_toolkits.openapi.spec import reduce_openapi_spec
from langchain_community.tools.json.tool import JsonSpec
from langchain_community.utilities import RequestsWrapper
from langchain_community.agent_toolkits import OpenAPIToolkit, create_openapi_agent
from langchain_community.agent_toolkits.openapi import planner
from dotenv import load_dotenv

load_dotenv()

from insight_src.utils.custom_prompts import PREFIX_PROMPT, SEVERITY_DEFINITION
from insight_src.utils import *
from insight_src.utils.validation import validate_cisco_api_token
from insight_src.utils import llm_connect


def construct_cisco_auth_headers(raw_spec: dict):
    validate_cisco_api_token()
    access_token = os.getenv("CISCO_API_BEARER_TOKEN")
    return {"Authorization": f"Bearer {access_token}"}


def getOpenAIJsonSpec():
    with open('./insight_src/utils/api_yaml/cisco_support_case_api_v3.yaml', 'r') as file:
        raw_openai_api_spec = yaml.safe_load(file)
        openai_api_spec = reduce_openapi_spec(raw_openai_api_spec)
        json_spec = JsonSpec(dict_=raw_openai_api_spec, max_value_length=4000)
        return openai_api_spec, json_spec, raw_openai_api_spec


PREFIX_CUSTOM_PROMPT = PREFIX_PROMPT.format(CISCO_USER_CCO=os.getenv(
    "CISCO_USER_CCO")) + SEVERITY_DEFINITION + """\n <Final Answer Formatting> For Final Answer after getting actual data, never provide dummy or example information, it need to start with `Final Answer: \n ` </Final Answer Formatting> """
USER_CISCO_CCO = os.getenv("CISCO_USER_CCO")


def getCaseData(userQuery: str):
    initialize()
    llm = llm_connect()
    from langchain_community.tools.json.tool import JsonSpec
    from insight_src.utils.validation import validate_cisco_api_token
    # Load the OpenAPI specification from your YAML file

    openapi_api_spec, json_spec, raw_openai_api_spec = getOpenAIJsonSpec()

    # Get API credentials.
    headers = construct_cisco_auth_headers(raw_openai_api_spec)
    requests_wrapper = RequestsWrapper(headers=headers)

    ALLOW_DANGEROUS_REQUEST = True
    openapi_toolkit = OpenAPIToolkit.from_llm(
        llm, json_spec, requests_wrapper, verbose=True, allow_dangerous_requests=ALLOW_DANGEROUS_REQUEST,
        base_url="https://apix.cisco.com//case/v3",
        handle_parse_errors=True
    )
    openapi_agent_executor = create_openapi_agent(
        llm=llm,
        toolkit=openapi_toolkit,
        allow_dangerous_requests=ALLOW_DANGEROUS_REQUEST,
        verbose=True,
        handle_parsing_errors=True,
        prefix=PREFIX_CUSTOM_PROMPT
    )
    return openapi_agent_executor.invoke(userQuery)
