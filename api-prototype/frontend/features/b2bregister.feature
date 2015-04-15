@RegisterName

Feature: Register a name

Scenario: Register a bankrupt using b2b
Given enter the bankruptcy details
When I submit search
Then I see the complete page
And I click Next for new registration

