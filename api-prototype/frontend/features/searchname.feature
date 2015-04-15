@searchByName

Feature: Search by Name

Scenario: Search using name 
Given enter name details
When I submit search
Then I see the result page
And I can reset form
