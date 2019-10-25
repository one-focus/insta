Feature: Login
  Check user can login with valid username and password

  Scenario: Invalid login1
    Given I login

    When I type "1234" in username field
    When I type "1234" in password field
    When I click element with text "Log in"
    Then I see element with text "The username you entered doesn't belong to an account."

    When I type "!@#$" in username field
    When I type "!@#$" in password field
    When I click element with text "Log in"
    Then I see element with text "The username you entered doesn't belong to an account."

  Scenario Outline: Invalid login2
    Given open login page
    When I type "<username>" in username field
    When I type "<password>" in password field
    When I click element with text "Log in"
    Then I see element with text "<text>"

    Examples:
      | username | password  | text                                                   |
      | sozdai   | qwer12313 | Sorry, your password was incorrect                     |
      | 1234     | 1234      | The username you entered doesn't belong to an account. |
      | !@#$     | !@#$      | The username you entered doesn't belong to an account. |


  Scenario: Invalid login3
    Given open login page
    Then I see validation message for
      | username | password | message                                                |
      | sozdai   | qwerqwe  | Sorry, your password was incorrect                     |
      | 1234qwe  | 1234qwe  | The username you entered doesn't belong to an account. |
      | !@#$     | !@#$     | The username you entered doesn't belong to an account. |
