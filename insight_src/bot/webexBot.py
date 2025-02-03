import logging
import os

from webexteamssdk import WebexTeamsAPI
from webex_bot.formatting import quote_info, quote_warning
from webex_bot.webex_bot import WebexBot
from webex_bot.models.command import Command
from webex_bot.models.response import response_from_adaptive_card
from webexpythonsdk.models.cards import AdaptiveCard, TextBlock, inputs, Choice, ChoiceSet, ActionSet, Image
from webexpythonsdk.models.cards.actions import Submit, ShowCard
from webexteamssdk.models.cards import ChoiceInputStyle

# Load environment variables
from dotenv import load_dotenv

load_dotenv()

from insight_src.apiAgent import getCaseData

logger = logging.getLogger(__name__)

class ProcessQuery(Command):

    def __init__(self):
        super().__init__(
            card_callback_keyword="process_query",
            delete_previous_message=True,
        )
        self.bot = WebexTeamsAPI(os.getenv("WEBEX_BOT_TOKEN"))

    def pre_execute(self, message, attachment_actions, activity):
        card = AdaptiveCard(
            body=[
                Image(url="https://i.postimg.cc/5Ny6GL5f/Loading.gif", altText="Loading...")
            ]
        )
        return response_from_adaptive_card(card)

    def execute(self, message, attachment_actions, activity):
        user_entered_query = attachment_actions.inputs.get("user_query")
        user_selected_query = attachment_actions.inputs.get("sample_queries")
        query = user_entered_query if user_entered_query else user_selected_query
        resp = getCaseData(query)
        return f"Query: {quote_warning(query)}\n\n Final Answer:{quote_info(resp.get('output'))}"


class QueryCommand(Command):
    def __init__(self):
        super().__init__(
            command_keyword="query",
            help_message="Helps to ask query to get TAC Insights",
            card=None,
            chained_commands=[ProcessQuery()]
        )

    def execute(self, message, attachment_actions, activity):
        card = AdaptiveCard(
            body=[
                TextBlock("Click below to expand and see sample queries and text box:"),
                ActionSet(
                    actions=[
                        ShowCard(
                            title="Sample Queries",
                            card=AdaptiveCard(
                                body=[
                                    ChoiceSet(
                                        id="sample_queries",
                                        style=ChoiceInputStyle.EXPANDED,
                                        choices=[
                                            Choice(title="List all cases with high severity", value="List all cases with high severity"),
                                            Choice(title="Give me all open cases and their current status",
                                                   value="Give me all open cases and their current status"),
                                            Choice(title="list all RMA for cases", value="list all RMA for cases"),
                                        ]
                                    ),
                                ],
                                actions=[
                                    Submit(title="Use Query", data={"callback_keyword": "process_query"})
                                ]
                            )
                        )
                    ]
                ),
                inputs.Text(id="user_query", placeholder="Enter your query here..."),
                ActionSet(
                    actions=[
                        Submit(title="Send", data={"callback_keyword": "process_query"})
                    ]
                )
            ]
        )
        return response_from_adaptive_card(card)

# Define the bot
def runnableBot(webex_bot_token: str = None) -> WebexBot:
    bot_token = os.getenv("WEBEX_BOT_TOKEN") if webex_bot_token is None else webex_bot_token
    approved_user = [e.strip() for e in os.getenv("ALLOW_WEBEX_USER_EMAIL").split(";")] if os.getenv("ALLOW_WEBEX_USER_EMAIL") else []
    bot = WebexBot(bot_token,
                   bot_name="Gen AI based TAC Insights",
                   bot_help_subtitle="This bot helps to ask query to get TAC Insights, ensure to provide Cisco Auth before using the bot",
                   approved_users=approved_user)

    # Add the command to the bot
    bot.add_command(QueryCommand())
    return bot


# Run the bot
if __name__ == "__main__":
    bot = runnableBot()
    bot.run()