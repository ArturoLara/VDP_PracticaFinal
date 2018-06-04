Feature: Web words analyzer
    In order to analyze a text in the web
    As users
    We'll implement a web that will use our words analyzer script

    Scenario: Analyze a normal text
      Given I have the text "Hola, me llamo Alfonso. Hola que tal, no me llamo Arturo."
      When I put it in the textfield
      And I click the execute button
      Then I see that text in the result text
            """
          me 2
          llamo 2
          hola 2
          no 1
          tal 1
          que 1
          alfonso 1
          arturo 1
      """
      And I see in the textfield the text ""

    Scenario: Analyze a empty text
      Given I have the text ""
      When I put it in the textfield
      And I click the execute button
      Then I see that text in the result text
    """
    """
      And I see in the textfield the text ""

    Scenario: Reset the textfield
      Given I have in the textfield the text "Esto va a ser reseteado"
      When I click the reset bottom
      Then I see in the textfield the text ""

    Scenario: Reset the empty textfield
      Given I have in the textfield the text ""
      When I click the reset bottom
      Then I see in the textfield the text ""

    Scenario: More than 100 characters at the textfield
      Given I have the text "0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789EstoNoSaldra"
      When I put it in the textfield the text
      And I click the execute button
      Then I see that text in the result text
            """
0123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789 1
      """
      And I see in the textfield the text ""
