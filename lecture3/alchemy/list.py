import os #operating system library

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")) #creating a database engine "an object created by SQL alchemy that is used to manage connections to the database
db = scoped_session(sessionmaker(bind=engine)) #once we take our web application to the internet and we have multiple people that are simultaneously trying to use our website at the same time, we wanna make sure that the stuff that person A is doing with the database is kept separate from the stuff that person B is doing with the database

def main():
	flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall() #feeding in SQL syntax into db.execute to say i want to run all of this SQL code
	for flight in flights: #running a loop
		print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes.") #so flight is the name of one of those individual rows. to get just the origin of that row, I use flight.origin 

if __name__ == "__main__":
	main()
	
#inside of flights(line10) i have a list of all the individual rows that came back from that SQL query.