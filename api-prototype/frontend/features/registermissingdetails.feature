@registerMissingDetails

Feature: Missing input on register

Scenario: Register with no details 
Given I enter no input details
When I submit search
Then I see errors

