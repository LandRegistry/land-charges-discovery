require 'capybara'
require 'capybara/dsl'
require 'capybara/rspec'
require 'rspec'
require 'capybara/cucumber'

Capybara.default_driver = :selenium

class AssertionFailure < RuntimeError
end

def assert( condition, message = nil )
    unless( condition )
        raise AssertionFailure, message
    end
end

When(/^I go to it's URL$/) do
    visit( 'http://localhost:5002/index' )
end


When (/^I submit search$/) do
    click_button('submit')
end
