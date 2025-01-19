Feature: Test Scenarios for filter functionality

Scenario: User can filter the Secondary deals by “want to sell” option
    Given Open the main page
    When Log in to the page
    And Click on “Secondary” option at the left side menu
    Then Verify the right page opens
    When Click on Filter
    And Filter the products by “want to sell”
    And Click on Apply Filter
    Then Verify all cards have “for sale” tag