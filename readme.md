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

## Licensing info

A license is required for others to be able to use your code. An open source license is more than just a usage license, it is license to contribute and collaborate on code. Open sourcing code and contributing it to [Code Exchange](https://developer.cisco.com/codeexchange/) requires a commitment to maintain the code and help the community use and contribute to the code. 

Choosing a license can be difficult and depend on your goals for your code, other licensed code on which your code depends, your business objectives, etc.   This template does not intend to provide legal advise. You should seek legal counsel for that. However, in general, less restrictive licenses make your code easier for others to use.

> Cisco employees can find licensing options and guidance [here](https://wwwin-github.cisco.com/DevNet/DevNet-Code-Exchange/blob/master/GitHubUsage.md#licensing-guidance).

Once you have determined which license is appropriate, GitHub provides functionality that makes it easy to add a LICENSE file to a GitHub repo, either when creating a new repo or by adding to an existing repo.

When creating a repo through the GitHub UI, you can click on *Add a license* and select from a set of [OSI approved open source licenses](https://opensource.org/licenses). See [detailed instructions](https://help.github.com/articles/licensing-a-repository/#applying-a-license-to-a-repository-with-an-existing-license).

Once a repo has been created, you can easily add a LICENSE file through the GitHub UI at any time. Simply select *Create New File*, type *LICENSE* into the filename box, and you will be given the option to select from a set of common open source licenses. See [detailed instructions](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository).

Once you have created the LICENSE file, be sure to update/replace any templated fields with appropriate information, including the Copyright. For example, the [3-Clause BSD license template](https://opensource.org/licenses/BSD-3-Clause) has the following copyright notice:

`Copyright (c) <YEAR>, <COPYRIGHT HOLDER>`

See the [LICENSE](./LICENSE) for this template repo as an example.

Once your LICENSE file exists, you can delete this section of the README, or replace the instructions in this section with a statement of which license you selected and a link to your license file, e.g.

This code is licensed under the BSD 3-Clause License. See [LICENSE](./LICENSE) for details.

Some licenses, such as Apache 2.0 and GPL v3, do not include a copyright notice in the [LICENSE](./LICENSE) itself. In such cases, a NOTICE file is a common place to include a copyright notice. For a very simple example, see [NOTICE](./NOTICE). 

In the event you make use of 3rd party code, it is required by some licenses, and a good practice in all cases, to provide attribution for all such 3rd party code in your NOTICE file. For a great example, see [https://github.com/cisco/ChezScheme/blob/main/NOTICE](https://github.com/cisco/ChezScheme/blob/main/NOTICE).  

[More about open-source licenses](https://github.com/CiscoDevNet/code-exchange-repo-template/blob/main/manual-sample-repo/open-source_license_guide.md)


