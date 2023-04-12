Feature: Add content form
  As a user
  I want to be welcome
  So that I know I am on the right spot

  Background:
    When Logo is displayed

  @regression
  Scenario Outline: Populated test
    Given Go to the form page
    When I enter first name "<first_name>"
    And I enter last name "<last_name>"
    And Click submit
    Then Success message will be displayed
    Examples:
      | first_name | last_name |
      | Gorodetchi | David     |
      | Tarata     | Andreea   |
      | Creanga    | Ion       |


