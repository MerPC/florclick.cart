Feature: cart price

  Scenario: check a cart price
    Given I go to homepage
    When I add an article "1" to the cart
    And I add an article "2" to the cart
    Then I can see the total price of the cart

