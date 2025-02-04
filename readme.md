# TAC Insights

TAC Insights is ascript which demonstrate how we can use LLM with Cisco Case API to get data and generate insight from the opened case

* Technology stack: Langchain, Python, Cisco Case API, OpenAI model
* Status:  Alpha

# Use Case

TAC insight helps to connect Cisco Case API in meaningful way to identify case, RMA, serial number daata.
It could be used by partner and customer with SNTC or PSS partner 


## Installation

Detailed instructions on how to install, configure, and get the project running. Call out any dependencies. This should be frequently tested and updated to make sure it works reliably, accounts for updated versions of dependencies, etc.

**Sample:**

Clone the repo
```bash
git clone https://github.com/vivlinux/tac_insight.git
```
Go to your project folder
```bash
cd tac_insight
```

Set up a Python venv
First make sure that you have Python 3 installed on your machine. We will then be using venv to create an isolated environment with only the necessary packages.

Install virtualenv via pip
```bash
pip install virtualenv
```

Create the venv
```bash
python3 -m venv venv
```

Activate your venv
```bash
source venv/bin/activate
```

Install dependencies
```bash
pip install -r requirements.txt
```

## Configuration (optional)

Ensure to copy .env.example file and configure the following:

```bash
cp .env.example .env
```
Set up following details:
1. Generate Cisco CASE API Client ID and Client Secret
2. Configure OpenAI Token
3. Configure OpenAI Model and Version
4. Configure Webex Token and Email format

#### Extracting Webex Token
1. Go to https://developer.webex.com/docs/api/getting-started
2. Click on "Get Started" and login with your Webex account
3. Click on "Create a Bot" and follow the instructions
4. Copy the Bot Token and paste at `WEBEX_BOT_TOKEN` in the .env file
5. Copy the email format and paste at `WEBEX_BOT_USERNAME` in the .env file
6. Save the .env file

#### Extract Cisco Case API Client ID and Client Secret
1. Go to https://apiconsole.cisco.com/
2. Click on "Create an App" and follow the instructions
3. Copy the Client ID and paste at `CISCO_API_CLIENT_ID` in the .env file
4. Copy the Client Secret and paste at `CISCO_API_CLIENT_SECRET` in the .env file
5. Save the .env file

#### Extract OpenAI Token
1. Go to https://platform.openai.com/docs/guides/authentication
2. Click on "Get Started" and follow the instructions
3. Copy the API Key and paste at `OPENAI_API_KEY` in the .env file
4. Provide Model such as `gpt-4` or `gpt-4o` and paste at `OPENAI_MODEL` in the .env file
5. Provide Model Version such as `2023-08-01-preview` and paste at `OPENAI_MODEL_VERSION` in the .env file
6. Save the .env file


## Usage
Run the service
```bash
make run
```

## How to test the software
1. Access the bot in Webex Teams
2. Type `help` to get the list of commands
3. Provide query or select query from the list of query

