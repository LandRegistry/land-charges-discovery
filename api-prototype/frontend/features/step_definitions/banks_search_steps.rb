Given(/^the app is running$/) do
end

Given (/^I enter no name details$/) do
  visit( 'http://localhost:5002/index' )
end

Given(/^enter name details$/) do
  visit( 'http://localhost:5002/index' )
  page.fill_in "forename", :with => "Jack"
  page.fill_in "surname", :with => "Bloggs"
end

Given(/^enter complex name details$/) do
  visit( 'http://localhost:5002/index' )
  page.fill_in "alternative", :with => "BRADFORD DIOCESAN BOARD OF FINANCE"
end

Then(/^I see the search page$/) do
    expect( page.has_css?( "div.form-group" ) ).to be true
end

Then (/^I see the result page$/) do
    page.should have_content("Search Results")
end


Then (/^I can reset form$/) do
  click_link('reset')
  page.should have_no_content("Search Results")
end

Then (/^I see error fields$/) do
    page.should have_content("Missing forename")
end

