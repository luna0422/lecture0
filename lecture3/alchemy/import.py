import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")) 
db = scoped_session(sessionmaker(bind=engine)) 

def main():
	f = open("flights.csv") #in flights.csv you have flights you want to add for example budapest,vienna,30
	reader = csv.reader(f)
	for origin, destination, duration in reader:
		db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)", #placeholders
				{"origin": origin, "destination": destination, "duration": duration}) #fill em in
		print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
	db.commit() #save the changes
	
if __name__ == "__main__":
	main()
	
