# don't run this file, but copy/paste lines into the shell to help with adding data

# next line in terminal to get into the shell
# python manage.py shell


from users.models import MyUser, UserProfile, Course
import random

thousandGirls = ['Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Camila', 'Gianna', 'Abigail', 'Luna', 'Ella', 'Elizabeth', 'Sofia', 'Emily', 'Avery',
				 'Mila', 'Scarlett', 'Eleanor', 'Madison', 'Layla', 'Penelope', 'Aria', 'Chloe', 'Grace', 'Ellie', 'Nora', 'Hazel', 'Zoey', 'Riley', 'Victoria', 'Lily', 'Aurora', 'Violet', 'Nova',
				 'Hannah', 'Emilia', 'Zoe', 'Stella', 'Everly', 'Isla', 'Leah', 'Lillian', 'Addison', 'Willow', 'Lucy', 'Paisley', 'Natalie', 'Naomi', 'Eliana', 'Brooklyn', 'Elena', 'Aubrey',
				 'Claire', 'Ivy', 'Kinsley', 'Audrey', 'Maya', 'Genesis', 'Skylar', 'Bella', 'Aaliyah', 'Madelyn', 'Savannah', 'Anna', 'Delilah', 'Serenity', 'Caroline', 'Kennedy', 'Valentina',
				 'Ruby', 'Sophie', 'Alice', 'Gabriella', 'Sadie', 'Ariana', 'Allison', 'Hailey', 'Autumn', 'Nevaeh', 'Natalia', 'Quinn', 'Josephine', 'Sarah', 'Cora', 'Emery', 'Samantha', 'Piper',
				 'Leilani', 'Eva', 'Everleigh', 'Madeline', 'Lydia', 'Jade', 'Peyton', 'Brielle', 'Adeline', 'Vivian', 'Rylee', 'Clara', 'Raelynn', 'Melanie', 'Melody', 'Julia', 'Athena', 'Maria',
				 'Liliana', 'Hadley', 'Arya', 'Rose', 'Reagan', 'Eliza', 'Adalynn', 'Kaylee', 'Lyla', 'Mackenzie', 'Alaia', 'Isabelle', 'Charlie', 'Arianna', 'Mary', 'Remi', 'Margaret', 'Iris',
				 'Parker', 'Ximena', 'Eden', 'Ayla', 'Kylie', 'Elliana', 'Josie', 'Katherine', 'Faith', 'Alexandra', 'Eloise', 'Adalyn', 'Amaya', 'Jasmine', 'Amara', 'Daisy', 'Reese', 'Valerie',
				 'Brianna', 'Cecilia', 'Andrea', 'Summer', 'Valeria', 'Norah', 'Ariella', 'Esther', 'Ashley', 'Emerson', 'Aubree', 'Isabel', 'Anastasia', 'Ryleigh', 'Khloe', 'Taylor', 'Londyn',
				 'Lucia', 'Emersyn', 'Callie', 'Sienna', 'Blakely', 'Kehlani', 'Genevieve', 'Alina', 'Bailey', 'Juniper', 'Maeve', 'Molly', 'Harmony', 'Georgia', 'Magnolia', 'Catalina', 'Freya',
				 'Juliette', 'Sloane', 'June', 'Sara', 'Ada', 'Kimberly', 'River', 'Ember', 'Juliana', 'Aliyah', 'Millie', 'Brynlee', 'Teagan', 'Morgan', 'Jordyn', 'London', 'Alaina', 'Olive',
				 'Rosalie', 'Alyssa', 'Ariel', 'Finley', 'Arabella', 'Journee', 'Hope', 'Leila', 'Alana', 'Gemma', 'Vanessa', 'Gracie', 'Noelle', 'Marley', 'Elise', 'Presley', 'Kamila', 'Zara', 'Amy',
				 'Kayla', 'Payton', 'Blake', 'Ruth', 'Alani', 'Annabelle', 'Sage', 'Aspen', 'Laila', 'Lila', 'Rachel', 'Trinity', 'Daniela', 'Alexa', 'Lilly', 'Lauren', 'Elsie', 'Margot', 'Adelyn',
				 'Zuri', 'Brooke', 'Sawyer', 'Lilah', 'Lola', 'Selena', 'Mya', 'Sydney', 'Diana', 'Ana', 'Vera', 'Alayna', 'Nyla', 'Elaina', 'Rebecca', 'Angela', 'Kali', 'Alivia', 'Raegan', 'Rowan',
				 'Phoebe', 'Camilla', 'Joanna', 'Malia', 'Vivienne', 'Dakota', 'Brooklynn', 'Evangeline', 'Camille', 'Jane', 'Nicole', 'Catherine', 'Jocelyn', 'Julianna', 'Lena', 'Lucille', 'Mckenna',
				 'Paige', 'Adelaide', 'Charlee', 'Mariana', 'Myla', 'Mckenzie', 'Tessa', 'Miriam', 'Oakley', 'Kailani', 'Alayah', 'Amira', 'Adaline', 'Phoenix', 'Milani', 'Annie', 'Lia', 'Angelina',
				 'Harley', 'Cali', 'Maggie', 'Hayden', 'Leia', 'Fiona', 'Briella', 'Journey', 'Lennon', 'Saylor', 'Jayla', 'Kaia', 'Thea', 'Adriana', 'Mariah', 'Juliet', 'Oaklynn', 'Kiara', 'Alexis',
				 'Haven', 'Aniyah', 'Delaney', 'Gracelynn', 'Kendall', 'Winter', 'Lilith', 'Logan', 'Amiyah', 'Evie', 'Alexandria', 'Gracelyn', 'Gabriela', 'Sutton', 'Harlow', 'Madilyn', 'Makayla',
				 'Evelynn', 'Gia', 'Nina', 'Amina', 'Giselle', 'Brynn', 'Blair', 'Amari', 'Octavia', 'Michelle', 'Talia', 'Demi', 'Alaya', 'Kaylani', 'Izabella', 'Fatima', 'Tatum', 'Makenzie',
				 'Lilliana', 'Arielle', 'Palmer', 'Melissa', 'Willa', 'Samara', 'Destiny', 'Dahlia', 'Celeste', 'Ainsley', 'Rylie', 'Reign', 'Laura', 'Adelynn', 'Gabrielle', 'Remington', 'Wren',
				 'Brinley', 'Amora', 'Lainey', 'Collins', 'Lexi', 'Aitana', 'Alessandra', 'Kenzie', 'Raelyn', 'Elle', 'Everlee', 'Haisley', 'Hallie', 'Wynter', 'Daleyza', 'Gwendolyn', 'Paislee',
				 'Ariyah', 'Veronica', 'Heidi', 'Anaya', 'Cataleya', 'Kira', 'Avianna', 'Felicity', 'Aylin', 'Miracle', 'Sabrina', 'Lana', 'Ophelia', 'Elianna', 'Royalty', 'Madeleine', 'Esmeralda',
				 'Joy', 'Kalani', 'Esme', 'Jessica', 'Leighton', 'Ariah', 'Makenna', 'Nylah', 'Viviana', 'Camryn', 'Cassidy', 'Dream', 'Luciana', 'Maisie', 'Stevie', 'Kate', 'Lyric', 'Daniella',
				 'Alicia', 'Daphne', 'Frances', 'Charli', 'Raven', 'Paris', 'Nayeli', 'Serena', 'Heaven', 'Bianca', 'Helen', 'Hattie', 'Averie', 'Mabel', 'Selah', 'Allie', 'Marlee', 'Kinley',
				 'Regina', 'Carmen', 'Jennifer', 'Jordan', 'Alison', 'Stephanie', 'Maren', 'Kayleigh', 'Angel', 'Annalise', 'Jacqueline', 'Braelynn', 'Emory', 'Rosemary', 'Scarlet', 'Amanda',
				 'Danielle', 'Emelia', 'Ryan', 'Carolina', 'Astrid', 'Kensley', 'Shiloh', 'Maci', 'Francesca', 'Rory', 'Celine', 'Kamryn', 'Zariah', 'Liana', 'Poppy', 'Maliyah', 'Keira', 'Skyler',
				 'Noa', 'Skye', 'Nadia', 'Addilyn', 'Rosie', 'Eve', 'Sarai', 'Edith', 'Jolene', 'Maddison', 'Meadow', 'Charleigh', 'Matilda', 'Elliott', 'Madelynn', 'Holly', 'Leona', 'Azalea',
				 'Katie', 'Mira', 'Ari', 'Kaitlyn', 'Danna', 'Cameron', 'Kyla', 'Bristol', 'Kora', 'Armani', 'Nia', 'Malani', 'Dylan', 'Remy', 'Maia', 'Dior', 'Legacy', 'Alessia', 'Shelby', 'Maryam',
				 'Sylvia', 'Yaretzi', 'Lorelei', 'Madilynn', 'Abby', 'Helena', 'Jimena', 'Elisa', 'Renata', 'Amber', 'Aviana', 'Carter', 'Emmy', 'Haley', 'Alondra', 'Elaine', 'Erin', 'April', 'Emely',
				 'Imani', 'Kennedi', 'Lorelai', 'Hanna', 'Kelsey', 'Aurelia', 'Colette', 'Jaliyah', 'Kylee', 'Macie', 'Aisha', 'Dorothy', 'Charley', 'Kathryn', 'Adelina', 'Adley', 'Monroe', 'Sierra',
				 'Ailani', 'Miranda', 'Mikayla', 'Alejandra', 'Amirah', 'Jada', 'Jazlyn', 'Jenna', 'Jayleen', 'Beatrice', 'Kendra', 'Lyra', 'Nola', 'Emberly', 'Mckinley', 'Myra', 'Katalina',
				 'Antonella', 'Zelda', 'Alanna', 'Amaia', 'Priscilla', 'Briar', 'Kaliyah', 'Itzel', 'Oaklyn', 'Alma', 'Mallory', 'Novah', 'Amalia', 'Fernanda', 'Alia', 'Angelica', 'Elliot', 'Justice',
				 'Mae', 'Cecelia', 'Gloria', 'Ariya', 'Virginia', 'Cheyenne', 'Aleah', 'Jemma', 'Henley', 'Meredith', 'Leyla', 'Lennox', 'Ensley', 'Zahra', 'Reina', 'Frankie', 'Lylah', 'Nalani',
				 'Reyna', 'Saige', 'Ivanna', 'Aleena', 'Emerie', 'Ivory', 'Leslie', 'Alora', 'Ashlyn', 'Bethany', 'Bonnie', 'Sasha', 'Xiomara', 'Salem', 'Adrianna', 'Dayana', 'Clementine', 'Karina',
				 'Karsyn', 'Emmie', 'Julie', 'Julieta', 'Briana', 'Carly', 'Macy', 'Marie', 'Oaklee', 'Christina', 'Malaysia', 'Ellis', 'Irene', 'Anne', 'Anahi', 'Mara', 'Rhea', 'Davina', 'Dallas',
				 'Jayda', 'Mariam', 'Skyla', 'Siena', 'Elora', 'Marilyn', 'Jazmin', 'Megan', 'Rosa', 'Savanna', 'Allyson', 'Milan', 'Coraline', 'Johanna', 'Melany', 'Chelsea', 'Michaela', 'Melina',
				 'Angie', 'Cassandra', 'Yara', 'Kassidy', 'Liberty', 'Lilian', 'Avah', 'Anya', 'Laney', 'Navy', 'Opal', 'Amani', 'Zaylee', 'Mina', 'Sloan', 'Romina', 'Ashlynn', 'Aliza', 'Liv',
				 'Malaya', 'Blaire', 'Janelle', 'Kara', 'Analia', 'Hadassah', 'Hayley', 'Karla', 'Chaya', 'Cadence', 'Kyra', 'Alena', 'Ellianna', 'Katelyn', 'Kimber', 'Laurel', 'Lina', 'Capri',
				 'Braelyn', 'Faye', 'Kamiyah', 'Kenna', 'Louise', 'Calliope', 'Kaydence', 'Nala', 'Tiana', 'Aileen', 'Sunny', 'Zariyah', 'Milana', 'Giuliana', 'Eileen', 'Elodie', 'Rayna', 'Monica',
				 'Galilea', 'Journi', 'Lara', 'Marina', 'Aliana', 'Harmoni', 'Jamie', 'Holland', 'Emmalyn', 'Lauryn', 'Chanel', 'Tinsley', 'Jessie', 'Lacey', 'Elyse', 'Janiyah', 'Jolie', 'Ezra',
				 'Marleigh', 'Roselyn', 'Lillie', 'Louisa', 'Madisyn', 'Penny', 'Kinslee', 'Treasure', 'Zaniyah', 'Estella', 'Jaylah', 'Khaleesi', 'Alexia', 'Dulce', 'Indie', 'Maxine', 'Waverly',
				 'Giovanna', 'Miley', 'Saoirse', 'Estrella', 'Greta', 'Rosalia', 'Mylah', 'Teresa', 'Bridget', 'Kelly', 'Adalee', 'Aubrie', 'Lea', 'Harlee', 'Anika', 'Itzayana', 'Hana', 'Kaisley',
				 'Mikaela', 'Naya', 'Avalynn', 'Margo', 'Sevyn', 'Florence', 'Keilani', 'Lyanna', 'Joelle', 'Kataleya', 'Royal', 'Averi', 'Kallie', 'Winnie', 'Baylee', 'Martha', 'Pearl', 'Alaiya',
				 'Rayne', 'Sylvie', 'Brylee', 'Jazmine', 'Ryann', 'Kori', 'Noemi', 'Haylee', 'Julissa', 'Celia', 'Laylah', 'Rebekah', 'Rosalee', 'Aya', 'Bria', 'Adele', 'Aubrielle', 'Tiffany',
				 'Addyson', 'Kai', 'Bellamy', 'Leilany', 'Princess', 'Chana', 'Estelle', 'Selene', 'Sky', 'Dani', 'Thalia', 'Ellen', 'Rivka', 'Amelie', 'Andi', 'Kynlee', 'Raina', 'Vienna', 'Alianna',
				 'Livia', 'Madalyn', 'Mercy', 'Novalee', 'Ramona', 'Vada', 'Berkley', 'Gwen', 'Persephone', 'Milena', 'Paula', 'Clare', 'Kairi', 'Linda', 'Paulina', 'Kamilah', 'Amoura', 'Hunter',
				 'Isabela', 'Karen', 'Marianna', 'Sariyah', 'Theodora', 'Annika', 'Kyleigh', 'Nellie', 'Scarlette', 'Keyla', 'Kailey', 'Mavis', 'Lilianna', 'Rosalyn', 'Sariah', 'Tori', 'Yareli',
				 'Aubriella', 'Bexley', 'Bailee', 'Jianna', 'Keily', 'Annabella', 'Azariah', 'Denisse', 'Promise', 'August', 'Hadlee', 'Halle', 'Fallon', 'Oakleigh', 'Zaria', 'Jaylin', 'Paisleigh',
				 'Crystal', 'Ila', 'Aliya', 'Cynthia', 'Giana', 'Maleah', 'Rylan', 'Aniya', 'Denise', 'Emmeline', 'Scout', 'Simone', 'Noah', 'Zora', 'Meghan', 'Landry', 'Ainhoa', 'Lilyana', 'Noor',
				 'Belen', 'Brynleigh', 'Cleo', 'Meilani', 'Karter', 'Amaris', 'Frida', 'Iliana', 'Violeta', 'Addisyn', 'Nancy', 'Denver', 'Leanna', 'Braylee', 'Kiana', 'Wrenley', 'Barbara', 'Khalani',
				 'Aspyn', 'Ellison', 'Judith', 'Robin', 'Valery', 'Aila', 'Deborah', 'Cara', 'Clarissa', 'Iyla', 'Lexie', 'Anais', 'Kaylie', 'Nathalie', 'Alisson', 'Della', 'Addilynn', 'Elsa', 'Zoya',
				 'Layne', 'Marlowe', 'Jovie', 'Kenia', 'Samira', 'Jaylee', 'Jenesis', 'Etta', 'Shay', 'Amayah', 'Avayah', 'Egypt', 'Flora', 'Raquel', 'Whitney', 'Zola', 'Giavanna', 'Raya', 'Veda',
				 'Halo', 'Paloma', 'Nataly', 'Whitley', 'Dalary', 'Drew', 'Guadalupe', 'Kamari', 'Esperanza', 'Loretta', 'Malayah', 'Natasha', 'Stormi', 'Ansley', 'Carolyn', 'Corinne', 'Paola',
				 'Brittany', 'Emerald', 'Freyja', 'Zainab', 'Artemis', 'Jillian', 'Kimora', 'Zoie', 'Aislinn', 'Emmaline', 'Ayleen', 'Queen', 'Jaycee', 'Murphy', 'Nyomi', 'Elina', 'Hadleigh',
				 'Marceline', 'Marisol', 'Yasmin', 'Zendaya', 'Chandler', 'Emani', 'Jaelynn', 'Kaiya', 'Nathalia', 'Violette', 'Joyce', 'Paityn', 'Elisabeth', 'Emmalynn', 'Luella', 'Yamileth',
				 'Aarya', 'Luisa', 'Zhuri', 'Araceli', 'Harleigh', 'Madalynn', 'Melani', 'Laylani', 'Magdalena', 'Mazikeen', 'Belle', 'Kadence']
thousandBoys = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Mason', 'Michael', 'Ethan', 'Daniel', 'Jacob', 'Logan', 'Jackson', 'Levi',
				'Sebastian', 'Mateo', 'Jack', 'Owen', 'Theodore', 'Aiden', 'Samuel', 'Joseph', 'John', 'David', 'Wyatt', 'Matthew', 'Luke', 'Asher', 'Carter', 'Julian', 'Grayson', 'Leo', 'Jayden',
				'Gabriel', 'Isaac', 'Lincoln', 'Anthony', 'Hudson', 'Dylan', 'Ezra', 'Thomas', 'Charles', 'Christopher', 'Jaxon', 'Maverick', 'Josiah', 'Isaiah', 'Andrew', 'Elias', 'Joshua', 'Nathan',
				'Caleb', 'Ryan', 'Adrian', 'Miles', 'Eli', 'Nolan', 'Christian', 'Aaron', 'Cameron', 'Ezekiel', 'Colton', 'Luca', 'Landon', 'Hunter', 'Jonathan', 'Santiago', 'Axel', 'Easton',
				'Cooper', 'Jeremiah', 'Angel', 'Roman', 'Connor', 'Jameson', 'Robert', 'Greyson', 'Jordan', 'Ian', 'Carson', 'Jaxson', 'Leonardo', 'Nicholas', 'Dominic', 'Austin', 'Everett', 'Brooks',
				'Xavier', 'Kai', 'Jose', 'Parker', 'Adam', 'Jace', 'Wesley', 'Kayden', 'Silas', 'Bennett', 'Declan', 'Waylon', 'Weston', 'Evan', 'Emmett', 'Micah', 'Ryder', 'Beau', 'Damian',
				'Brayden', 'Gael', 'Rowan', 'Harrison', 'Bryson', 'Sawyer', 'Amir', 'Kingston', 'Jason', 'Giovanni', 'Vincent', 'Ayden', 'Chase', 'Myles', 'Diego', 'Nathaniel', 'Legend', 'Jonah',
				'River', 'Tyler', 'Cole', 'Braxton', 'George', 'Milo', 'Zachary', 'Ashton', 'Luis', 'Jasper', 'Kaiden', 'Adriel', 'Gavin', 'Bentley', 'Calvin', 'Zion', 'Juan', 'Maxwell', 'Max',
				'Ryker', 'Carlos', 'Emmanuel', 'Jayce', 'Lorenzo', 'Ivan', 'Jude', 'August', 'Kevin', 'Malachi', 'Elliott', 'Rhett', 'Archer', 'Karter', 'Arthur', 'Luka', 'Elliot', 'Thiago',
				'Brandon', 'Camden', 'Justin', 'Jesus', 'Maddox', 'King', 'Theo', 'Enzo', 'Matteo', 'Emiliano', 'Dean', 'Hayden', 'Finn', 'Brody', 'Antonio', 'Abel', 'Alex', 'Tristan', 'Graham',
				'Zayden', 'Judah', 'Xander', 'Miguel', 'Atlas', 'Messiah', 'Barrett', 'Tucker', 'Timothy', 'Alan', 'Edward', 'Leon', 'Dawson', 'Eric', 'Ace', 'Victor', 'Abraham', 'Nicolas', 'Jesse',
				'Charlie', 'Patrick', 'Walker', 'Joel', 'Richard', 'Beckett', 'Blake', 'Alejandro', 'Avery', 'Grant', 'Peter', 'Oscar', 'Matias', 'Amari', 'Lukas', 'Andres', 'Arlo', 'Colt', 'Adonis',
				'Kyrie', 'Steven', 'Felix', 'Preston', 'Marcus', 'Holden', 'Emilio', 'Remington', 'Jeremy', 'Kaleb', 'Brantley', 'Bryce', 'Mark', 'Knox', 'Israel', 'Phoenix', 'Kobe', 'Nash',
				'Griffin', 'Caden', 'Kenneth', 'Kyler', 'Hayes', 'Jax', 'Rafael', 'Beckham', 'Javier', 'Maximus', 'Simon', 'Paul', 'Omar', 'Kaden', 'Kash', 'Lane', 'Bryan', 'Riley', 'Zane', 'Louis',
				'Aidan', 'Paxton', 'Maximiliano', 'Karson', 'Cash', 'Cayden', 'Emerson', 'Tobias', 'Ronan', 'Brian', 'Dallas', 'Bradley', 'Jorge', 'Walter', 'Josue', 'Khalil', 'Damien', 'Jett',
				'Kairo', 'Zander', 'Andre', 'Cohen', 'Crew', 'Hendrix', 'Colin', 'Chance', 'Malakai', 'Clayton', 'Daxton', 'Malcolm', 'Lennox', 'Martin', 'Jaden', 'Kayson', 'Bodhi', 'Francisco',
				'Cody', 'Erick', 'Kameron', 'Atticus', 'Dante', 'Jensen', 'Cruz', 'Finley', 'Brady', 'Joaquin', 'Anderson', 'Gunner', 'Muhammad', 'Zayn', 'Derek', 'Raymond', 'Kyle', 'Angelo', 'Reid',
				'Spencer', 'Nico', 'Jaylen', 'Jake', 'Prince', 'Manuel', 'Ali', 'Gideon', 'Stephen', 'Ellis', 'Orion', 'Rylan', 'Eduardo', 'Mario', 'Rory', 'Cristian', 'Odin', 'Tanner', 'Julius',
				'Callum', 'Sean', 'Kane', 'Ricardo', 'Travis', 'Wade', 'Warren', 'Fernando', 'Titus', 'Leonel', 'Edwin', 'Cairo', 'Corbin', 'Dakota', 'Ismael', 'Colson', 'Killian', 'Major', 'Tate',
				'Gianni', 'Elian', 'Remy', 'Lawson', 'Niko', 'Nasir', 'Kade', 'Armani', 'Ezequiel', 'Marshall', 'Hector', 'Desmond', 'Kason', 'Garrett', 'Jared', 'Cyrus', 'Russell', 'Cesar', 'Tyson',
				'Malik', 'Donovan', 'Jaxton', 'Cade', 'Romeo', 'Nehemiah', 'Sergio', 'Iker', 'Caiden', 'Jay', 'Pablo', 'Devin', 'Jeffrey', 'Otto', 'Kamari', 'Ronin', 'Johnny', 'Clark', 'Ari', 'Marco',
				'Edgar', 'Bowen', 'Jaiden', 'Grady', 'Zayne', 'Sullivan', 'Jayceon', 'Sterling', 'Andy', 'Conor', 'Raiden', 'Royal', 'Royce', 'Solomon', 'Trevor', 'Winston', 'Emanuel', 'Finnegan',
				'Pedro', 'Luciano', 'Harvey', 'Franklin', 'Noel', 'Troy', 'Princeton', 'Johnathan', 'Erik', 'Fabian', 'Oakley', 'Rhys', 'Porter', 'Hugo', 'Frank', 'Damon', 'Kendrick', 'Mathias',
				'Milan', 'Peyton', 'Wilder', 'Callan', 'Gregory', 'Seth', 'Matthias', 'Briggs', 'Ibrahim', 'Roberto', 'Conner', 'Quinn', 'Kashton', 'Sage', 'Santino', 'Kolton', 'Alijah', 'Dominick',
				'Zyaire', 'Apollo', 'Kylo', 'Reed', 'Philip', 'Kian', 'Shawn', 'Kaison', 'Leonidas', 'Ayaan', 'Lucca', 'Memphis', 'Ford', 'Baylor', 'Kyson', 'Uriel', 'Allen', 'Collin', 'Ruben',
				'Archie', 'Dalton', 'Esteban', 'Adan', 'Forrest', 'Alonzo', 'Isaias', 'Leland', 'Jase', 'Dax', 'Kasen', 'Gage', 'Kamden', 'Marcos', 'Jamison', 'Francis', 'Hank', 'Alexis', 'Tripp',
				'Frederick', 'Jonas', 'Stetson', 'Cassius', 'Izaiah', 'Eden', 'Maximilian', 'Rocco', 'Tatum', 'Keegan', 'Aziel', 'Moses', 'Bruce', 'Lewis', 'Braylen', 'Omari', 'Mack', 'Augustus',
				'Enrique', 'Armando', 'Pierce', 'Moises', 'Asa', 'Shane', 'Emmitt', 'Soren', 'Dorian', 'Keanu', 'Zaiden', 'Raphael', 'Deacon', 'Abdiel', 'Kieran', 'Phillip', 'Ryland', 'Zachariah',
				'Casey', 'Zaire', 'Albert', 'Baker', 'Corey', 'Kylan', 'Denver', 'Gunnar', 'Jayson', 'Drew', 'Callen', 'Jasiah', 'Drake', 'Kannon', 'Braylon', 'Sonny', 'Bo', 'Moshe', 'Huxley',
				'Quentin', 'Rowen', 'Santana', 'Cannon', 'Kenzo', 'Wells', 'Julio', 'Nikolai', 'Conrad', 'Jalen', 'Makai', 'Benson', 'Derrick', 'Gerardo', 'Davis', 'Abram', 'Mohamed', 'Ronald',
				'Raul', 'Arjun', 'Dexter', 'Kaysen', 'Jaime', 'Scott', 'Lawrence', 'Ariel', 'Skyler', 'Danny', 'Roland', 'Chandler', 'Yusuf', 'Samson', 'Case', 'Zain', 'Roy', 'Rodrigo', 'Sutton',
				'Boone', 'Saint', 'Saul', 'Jaziel', 'Hezekiah', 'Alec', 'Arturo', 'Jamari', 'Jaxtyn', 'Julien', 'Koa', 'Reece', 'Landen', 'Koda', 'Darius', 'Sylas', 'Ares', 'Kyree', 'Boston', 'Keith',
				'Taylor', 'Johan', 'Edison', 'Sincere', 'Watson', 'Jerry', 'Nikolas', 'Quincy', 'Shepherd', 'Brycen', 'Marvin', 'Dariel', 'Axton', 'Donald', 'Bodie', 'Finnley', 'Onyx', 'Rayan',
				'Raylan', 'Brixton', 'Colby', 'Shiloh', 'Valentino', 'Layton', 'Trenton', 'Landyn', 'Alessandro', 'Ahmad', 'Gustavo', 'Ledger', 'Ridge', 'Ander', 'Ahmed', 'Kingsley', 'Issac',
				'Mauricio', 'Tony', 'Leonard', 'Mohammed', 'Uriah', 'Duke', 'Kareem', 'Lucian', 'Marcelo', 'Aarav', 'Leandro', 'Reign', 'Clay', 'Kohen', 'Dennis', 'Samir', 'Ermias', 'Otis', 'Emir',
				'Nixon', 'Ty', 'Sam', 'Fletcher', 'Wilson', 'Dustin', 'Hamza', 'Bryant', 'Flynn', 'Lionel', 'Mohammad', 'Cason', 'Jamir', 'Aden', 'Dakari', 'Justice', 'Dillon', 'Layne', 'Zaid',
				'Alden', 'Nelson', 'Devon', 'Titan', 'Chris', 'Khari', 'Zeke', 'Noe', 'Alberto', 'Roger', 'Brock', 'Rex', 'Quinton', 'Alvin', 'Cullen', 'Azariah', 'Harlan', 'Kellan', 'Lennon',
				'Marcel', 'Keaton', 'Morgan', 'Ricky', 'Trey', 'Karsyn', 'Langston', 'Miller', 'Chaim', 'Salvador', 'Amias', 'Tadeo', 'Curtis', 'Lachlan', 'Amos', 'Anakin', 'Krew', 'Tomas',
				'Jefferson', 'Yosef', 'Bruno', 'Korbin', 'Augustine', 'Cayson', 'Mathew', 'Vihaan', 'Jamie', 'Clyde', 'Brendan', 'Jagger', 'Carmelo', 'Harry', 'Nathanael', 'Mitchell', 'Darren', 'Ray',
				'Jedidiah', 'Jimmy', 'Lochlan', 'Bellamy', 'Eddie', 'Rayden', 'Reese', 'Stanley', 'Joe', 'Houston', 'Douglas', 'Vincenzo', 'Casen', 'Emery', 'Joziah', 'Leighton', 'Marcellus',
				'Atreus', 'Aron', 'Hugh', 'Musa', 'Tommy', 'Alfredo', 'Junior', 'Neil', 'Westley', 'Banks', 'Eliel', 'Melvin', 'Maximo', 'Briar', 'Colten', 'Lance', 'Nova', 'Trace', 'Axl', 'Ramon',
				'Vicente', 'Brennan', 'Caspian', 'Remi', 'Deandre', 'Legacy', 'Lee', 'Valentin', 'Ben', 'Louie', 'Westin', 'Wayne', 'Benicio', 'Grey', 'Zayd', 'Gatlin', 'Mekhi', 'Orlando', 'Bjorn',
				'Harley', 'Alonso', 'Rio', 'Aldo', 'Byron', 'Eliseo', 'Ernesto', 'Talon', 'Thaddeus', 'Brecken', 'Kace', 'Kellen', 'Enoch', 'Kiaan', 'Lian', 'Creed', 'Rohan', 'Callahan', 'Jaxxon',
				'Ocean', 'Crosby', 'Dash', 'Gary', 'Mylo', 'Ira', 'Magnus', 'Salem', 'Abdullah', 'Kye', 'Tru', 'Forest', 'Jon', 'Misael', 'Madden', 'Braden', 'Carl', 'Hassan', 'Emory', 'Kristian',
				'Alaric', 'Ambrose', 'Dario', 'Allan', 'Bode', 'Boden', 'Juelz', 'Kristopher', 'Genesis', 'Idris', 'Ameer', 'Anders', 'Darian', 'Kase', 'Aryan', 'Dane', 'Guillermo', 'Elisha',
				'Jakobe', 'Thatcher', 'Eugene', 'Ishaan', 'Larry', 'Wesson', 'Yehuda', 'Alvaro', 'Bobby', 'Bronson', 'Dilan', 'Kole', 'Kyro', 'Tristen', 'Blaze', 'Brayan', 'Jadiel', 'Kamryn',
				'Demetrius', 'Maurice', 'Arian', 'Kabir', 'Rocky', 'Rudy', 'Randy', 'Rodney', 'Yousef', 'Felipe', 'Robin', 'Aydin', 'Dior', 'Kaiser', 'Van', 'Brodie', 'London', 'Eithan', 'Stefan',
				'Ulises', 'Camilo', 'Branson', 'Jakari', 'Judson', 'Yahir', 'Zavier', 'Damari', 'Jakob', 'Jaxx', 'Bentlee', 'Cain', 'Niklaus', 'Rey', 'Zahir', 'Aries', 'Blaine', 'Kyng', 'Castiel',
				'Henrik', 'Joey', 'Khalid', 'Bear', 'Graysen', 'Jair', 'Kylen', 'Darwin', 'Alfred', 'Ayan', 'Kenji', 'Zakai', 'Avi', 'Cory', 'Fisher', 'Jacoby', 'Osiris', 'Harlem', 'Jamal', 'Santos',
				'Wallace', 'Brett', 'Fox', 'Leif', 'Maison', 'Reuben', 'Adler', 'Zev', 'Calum', 'Kelvin', 'Zechariah', 'Bridger', 'Mccoy', 'Seven', 'Shepard', 'Azrael', 'Leroy', 'Terry', 'Harold',
				'Mac', 'Mordechai', 'Ahmir', 'Cal', 'Franco', 'Trent', 'Blaise', 'Coen', 'Dominik', 'Marley', 'Davion', 'Jeremias', 'Riggs', 'Jones', 'Will', 'Damir', 'Dangelo', 'Canaan', 'Dion',
				'Jabari', 'Landry', 'Salvatore', 'Kody', 'Hakeem', 'Truett', 'Gerald', 'Lyric', 'Gordon', 'Jovanni', 'Kamdyn', 'Alistair', 'Cillian', 'Foster', 'Terrance', 'Murphy', 'Zyair', 'Cedric',
				'Rome', 'Abner', 'Colter', 'Dayton', 'Jad', 'Xzavier', 'Rene', 'Vance', 'Duncan', 'Frankie', 'Bishop', 'Davian', 'Everest', 'Heath', 'Jaxen', 'Marlon', 'Maxton', 'Reginald', 'Harris',
				'Jericho', 'Keenan', 'Korbyn', 'Wes', 'Eliezer', 'Jeffery', 'Kalel', 'Kylian', 'Turner', 'Willie', 'Rogelio', 'Ephraim']
first_names = thousandGirls + thousandBoys
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzales', 'Wilson', 'Anderson', 'Thomas', 'Taylor',
		'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King', 'Wright', 'Scott',
		'Torres', 'Nguyen', 'Hill', 'Flores', 'Green', 'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell', 'Carter', 'Roberts', 'Gomez', 'Phillips', 'Evans', 'Turner', 'Diaz',
		'Parker', 'Cruz', 'Edwards', 'Collins', 'Reyes', 'Stewart', 'Morris', 'Morales', 'Murphy', 'Cook', 'Rogers', 'Gutierrez', 'Ortiz', 'Morgan', 'Cooper', 'Peterson', 'Bailey', 'Reed',
		'Kelly', 'Howard', 'Ramos', 'Kim', 'Cox', 'Ward', 'Richardson', 'Watson', 'Brooks', 'Chavez', 'Wood', 'James', 'Bennet', 'Gray', 'Mendoza', 'Ruiz', 'Hughes', 'Price', 'Alvarez',
		'Castillo', 'Sanders', 'Patel', 'Myers', 'Long', 'Ross', 'Foster', 'Jimenez']
area_codes = ['814', '717', '570', '412', '484']
belts = ['White', 'Yellow', 'Green', 'Brown', 'Blue', 'Red', 'Black']
cities = ['Bellefonte', 'State College', 'Altoona', 'Pleasant Gap', 'Milesburg', 'Zion', 'Centre Hall', 'Boalsburg']



def create_user(n):
	for _ in range(n):
		first = random.choice(first_names)
		last = random.choice(last_names)
		username = f'{first}.{last}{random.randint(1000, 9999)}'
		email = f'{username}@test.com'
		# created
		is_active = True
		is_staff = False
		is_superuser = False
		# user
		phone = f'({random.choice(area_codes)}){random.randint(2, 9)}{random.randint(1, 9)}{random.randint(1, 9)}-{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}{random.randint(1, 9)}'
		about = f'{random.choices(belts, weights=(13, 20, 17, 25, 12, 8, 5), k=1)[0]} belt. {random.randint(7, 70)} years old.'
		location = f'{random.choice(cities)}'
		is_instructor = False
		user = MyUser.objects.create(email=email, username=username, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser)
		user.set_password('a')
		user.save()
		profile = UserProfile.objects.last()
		profile.first = first
		profile.last = last
		profile.phone = phone
		profile.about = about
		profile.location = location
		profile.is_instructor = is_instructor
		profile.save()



course = Course.objects.create()
course.name = 'Little Tigers'
course.time = 'Friday at 5pm and 6pm'
course.ages = 'Ages 4 to 7'
course.cost = '$40'
course.description = ' '
course.save()

course = Course.objects.create()
course.name = 'Tae Kwon Do Beginner Kids'
course.time = 'Monday and Wednesday at 5pm to 6pm'
course.ages = 'Ages 7 to 12'
course.cost = '$79'
course.description = ' '
course.save()

course = Course.objects.create()
course.name = 'Tae Kwon Do Beginner Adult'
course.time = 'Mon/Wed at 7pm to 8pm and Tue/Thr Noon to 1pm'
course.ages = 'Ages 12 through Adult'
course.cost = '$79'
course.description = ' '
course.save()

course = Course.objects.create()
course.name = 'Aikido Beginner-Advanced'
course.time = 'Sunday Afternoons'
course.ages = 'Kids and Adults'
course.cost = '$30'
course.description = ' '
course.save()

course = Course.objects.create()
course.name = 'Jujitsu'
course.time = 'Tuesday and Thursday from 8pm to 9pm'
course.ages = 'Beginner to Advanced'
course.cost = '$75'
course.description = ' '
course.save()

course = Course.objects.create()
course.name = 'Advanced Tae Kwon Do'
course.time = 'Various Times'
course.ages = 'Advanced'
course.cost = '$79'
course.description = 'See instructors for more details for returning students or experienced students seeking a new school.'
course.save()
