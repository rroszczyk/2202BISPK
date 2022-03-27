Feature: My Juice

  Scenario: Blenders
    Given I put "apple" in a blender
    When  I switch the blender on
    Then  it should transform into "apple juice"