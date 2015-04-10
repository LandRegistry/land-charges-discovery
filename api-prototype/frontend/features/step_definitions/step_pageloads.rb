Given(/^the app is running$/) do
end

Then(/^I see the search page$/) do
    expect( page.has_css?( "div.form-group" ) ).to be true
end
