@searchComplexName

Feature: Search for Complex Name

Scenario: Search using complex name 
Given enter complex name details
When I submit search
Then I see the result page
And I can reset form
