@searchMissingName

Feature: Missing name on input

Scenario: Search no name 
Given I enter no name details
When I submit search
Then I see error fields

