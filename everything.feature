Feature: Tesing Doodle
	Scenario Outline: test something
		When I enter occasion integracja
		And I click submit
		And I click close modal button
		And I enter location Wroclaw
		And I click continue button
		And I choose date <day>
		And I click continue button
		And I enter credentials Gosia m.staniszew@gmail.com
		And I click finish button
		Then I am on the finish page

		Examples:
			| day |
			| 15  |
			| 16  |
	
 
	Scenario: test funeral
		When I enter occasion pogrzeb
		And I click submit
		And I click close modal button
		And I enter location Lodz
		And I click continue button
		And I choose date 15
		And I click continue button
		And I enter credentials Malgorzata malgorzata.staniszewska@stxnext.pl
		And I click finish button
		Then I am on the finish page