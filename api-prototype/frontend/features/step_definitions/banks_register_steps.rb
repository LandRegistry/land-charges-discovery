Given(/^enter the bankruptcy details$/) do
  visit( 'http://localhost:5002/insolvency' )
  page.fill_in "name", :with => "Harry Hopkins"
  page.fill_in "address", :with => "32 high street, PLymouth"
  page.fill_in "nature", :with => "pab"
end

Then (/^I see the complete page$/) do
    page.should have_content("Registration Complete")
end

Then (/^I click Next for new registration$/) do
  click_link('Next')
  page.should have_no_content("Registration Complete")
end

Given(/^I enter no input details$/) do
  visit( 'http://localhost:5002/insolvency' )
end

Then (/^I see errors$/) do
    page.should have_content("Missing")
end
