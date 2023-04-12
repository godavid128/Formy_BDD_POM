Feature: Add content form
  As a user
  I want to be welcome
  So that I know I am on the right spot

  Background:
    When Logo is displayed

  @smoke
  Scenario: Test transition is ok
    Given Go to the form page
    Then The form should be displayed
    When Go to the home page
    Then The home page be displayed

# todo implementarea celorlalte feature files - tot ce trebuie sa folosim sete din pagini