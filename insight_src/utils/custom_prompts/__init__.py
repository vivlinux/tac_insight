PREFIX_PROMPT="""
<Rules>

## MUST BE FOLLOWED PII Considerations
1. In final response, always replace case number or case id with format 6xxxxxxxx, serial number, contract number, and any other PII information  with  first 2 digit and followed by `***`
2. Replace any information for `Contact Name` with `***`

## Rules to identify the API
### Specific User query modification
1. For all query, add to the query `for user {CISCO_USER_CCO}` if user doesn't provide specific case numbers or serial numbers or contract numbers
_Example Query_
<Example>
_Query 1_
Original Query: "Show me all my open cases with the case title, contact names, severity, and current status. If an RMA or bug is associated with the case, the list this as well"
Modified Query: "Show me all my open cases with the case title, contact names, severity, and current status. If an RMA or bug is associated with the case, the list this as well for user {CISCO_USER_CCO}"

_Query 2_:
Original Query: "List all my high severity cases along with the current status and how long they have been opened for"
Modified Query: "List all my high severity cases along with the current status and how long they have been opened for for user {CISCO_USER_CCO}"
</Example>

Api Path: `/cases/users/user_ids/<user_ids>`

2. Specific Case number [format which starts with `6` followed by 8 numbers] required in the query to use this API

API Path to get Case Summary: `/cases/case_ids/<case_ids>`

There are other API Path wich can also be used to get the required information, please refer to the API documentation for more details
</Rules>

<Query Examples>
**Type 1: Specific User query modification**
Some query are very specific and require specific case numbers or serial numbers or contract numbers to get the required information. Here are some examples:
_Query 1_: Check case status for case number 60000001
_Query 2_: Get case summary for case number 60000001
_Query 3_: Check the RMA number in the case 60000001

**Type 2: Query require multiple steps**
_Query 1_: List all cases with high severity and their current status
_Steps_:
a. First call API to get cases based on the user
b. Identify API get severity and case status

_Query 2_: Get RMA or bug for all open case
_Steps_:
a. First call API to get cases based on the user
b. Identify API to get RMA or bug for the case using case API

</Query Examples>
"""

SEVERITY_DEFINITION = """
<Severity Definition>
Severity 1 - Critical impact on the customer’s business operations. Cisco’s hardware, software or "as a service" product is down.
Severity 2 - Substantial impact on the customer’s business operations. Cisco hardware, software or "as a service" product is degraded.
Severity 3 - Minimal impact on the customer’s business operations. Cisco hardware, software or "as a service" product is partially degraded.
Severity 4 - No impact on the customer’s business operations. The customer requests information about features, implementation, or configuration for Cisco’s hardware, software, or "as a service" product.
"Priority" and "Severity" are interchangeable. "High priority/severity" refers to Severity 1 or 2. "Low severity" refers to Severity 3 or 4. "Sev" is shorthand for "Severity".
If critical or severe cases are requested, then this means cases with a Priority equal to '1' or '2'.
A case's Priority can change over time. The Priority field refers to a cases current status. The Highest_Priority__c refers to the highest priority or severity that the case has attained during its lifetime.
</Severity Definition>
"""
