Feature: Create a new user

  Scenario: Successfully create a new user
    Given the user payload is prepared
    When the user is created
    Then the user creation should be successful
    And the user should be in the user list