Feature: Verify if Books are added and deleted using Library API
  @Library
  Scenario: Verify Addbook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook Post API method
    Then Book is sucessfully added
    And status code of response should be 200

    @Library
    Scenario Outline: Verify Addbook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook Post API method
    Then Book is sucessfully added
     Examples:
      |isbn         |aisle |
      |hondacb350XR |12966 |
      |RTR          |14047 |
