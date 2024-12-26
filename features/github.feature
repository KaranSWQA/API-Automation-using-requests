Feature: GitHub API validation
  Scenario: Session management check
    Given I have github auth credentails
    When I hit getRepo API of github
    Then status code of response should be 200
