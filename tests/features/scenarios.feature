Feature: Web words analyzer
    In order to see how many words are typing by day
    As users
    We'll implement a web that will use a url to get text and save it in a data base


    Scenario: Analyze a normal url
      Given I have the text "url_to_mock.html"
      When I put it in the url textfield
      And I click the execute button
      Then I see that text in the result text
            """
          me 2
          llamo 2
          hola 2
      """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""

    Scenario: Analyze a empty url text
      Given I have the text ""
      When I put it in the url textfield
      And I click the execute button
      Then I see that text in the result text
    """
    """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""



    Scenario: Analyze a empty url text
      Given I have the text ""
      When I put it in the date textfield
      And I click the seeDate button
      Then I see that text in the result text
    """
    """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""


    Scenario: Invalid url
      Given I have the text "invalidUrl"
      And I make sure that this url is invalid
      When I put it in the url textfield
      And I click the execute button
      Then I see that text in the result text
    """
    No se ha podido leer la pagina...
    """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""

    Scenario: Invalid date
      Given I have the text "invalidDate"
      When I put it in the date textfield
      And I click the seeDate button
      Then I see that text in the result text
    """
    """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""

    Scenario: Analyze a normal date
      Given I have the text "2018-06-05"
      When I put it in the date textfield
      And I click the seeDate button
      Then I see that text in the result text
            """
          me 2
          llamo 2
          hola 2
      """
      And I see in the url textfield the text ""
      And I see in the date textfield the text ""

    Scenario: With 2 textfield not empty, and click execute, both are empty
      Given I have the text "Lo que sea"
      When I put it in the date textfield
      And I put it in the url textfield
      And I click the execute button
      Then I see in the url textfield the text ""
      And I see in the date textfield the text ""


    Scenario: With 2 textfield not empty, and click seeDate, both are empty
      Given I have the text "Lo que sea"
      When I put it in the date textfield
      And I put it in the url textfield
      And I click the seeDate button
      Then I see in the url textfield the text ""
      And I see in the date textfield the text ""
