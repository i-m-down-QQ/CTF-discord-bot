from datetime import datetime, timedelta

import nextcord

from .params import DEFAULT_IMAGE_URL


class CTFEvent():
	def __init__(self):
		self.id = -1
		self.name = ""
		self.organizers = []
		self.logo = DEFAULT_IMAGE_URL
		self.ctftime_url = ""
		self.url = ""
		self.description = ""
		self.format = "None"
		self.location = "None"
		self.participants = -1
		self.restriction = "None"
		self.startTime = datetime.utcfromtimestamp(0)
		self.endTime = datetime.utcfromtimestamp(0)
		self.duration = timedelta(seconds=0)
		self.weight = -1
		self.is_votable_now = False
		self.public_votable = False

def parseCTFEvent(ctfData: dict) -> CTFEvent:
	"""
	Parse single CTF json data to CTFEvent class.
	"""
	event = CTFEvent()
	event.id = int(ctfData["id"])
	event.name = ctfData["title"]
	event.organizers = [o["name"] for o in ctfData["organizers"]]
	event.logo = DEFAULT_IMAGE_URL if ctfData["logo"] == "" else ctfData["logo"]
	event.ctftime_url = ctfData["ctftime_url"]
	event.url = ctfData["url"]
	event.description = ctfData["description"]
	event.format = ctfData["format"]
	event.location = ctfData["location"] if ctfData["onsite"] else "Online"
	event.participants = int(ctfData["participants"])
	event.restriction = "None" if ctfData["restrictions"] == "Open" else ctfData["restrictions"]
	event.startTime = datetime.fromisoformat(ctfData["start"])
	event.endTime = datetime.fromisoformat(ctfData["finish"])
	event.duration = timedelta(days=ctfData['duration']['days'], hours=ctfData['duration']['hours'])
	event.weight = int(ctfData["weight"])
	event.is_votable_now = bool(ctfData["is_votable_now"])
	event.public_votable = bool(ctfData["public_votable"])
	return event

def createEmbed(event: CTFEvent, is_running=False) -> nextcord.Embed:
	"""
	Create nextcord.Embed from CTFEvent
	"""
	embed = nextcord.Embed(
		title = event.name, 
		description= event.description,
		url = event.url
	)
	embed.set_thumbnail(url=event.logo)
	embed.add_field(name="Origanizers", value=", ".join(event.organizers), inline=True)
	embed.add_field(name="Location", value=event.location, inline=True)
	embed.add_field(name="Format", value=event.format, inline=True)
	embed.add_field(name="Weight", value=str(event.weight), inline=True)
	if(is_running):
		now = datetime.now(tz=event.endTime.tzinfo)
		endTime = event.endTime
		remainTime = endTime - now
		embed.add_field(
			name="Remain time", 
			value=f"{remainTime.days} days {remainTime.seconds // 3600} hours {(remainTime.seconds // 60) % 60} minutes", 
			inline=True
		)
		embed.add_field(name="End At (in your timezone)", value=f"<t:{int(event.endTime.timestamp())}>", inline=True)
	else:
		embed.add_field(name="Duration", value=f"{event.duration.days} days {event.duration.seconds // 3600} hours", inline=True)
		embed.add_field(
			name="Date (in your timezone)", 
			value=f"<t:{int(event.startTime.timestamp())}>\n~\n<t:{int(event.endTime.timestamp())}>", 
			inline=True
		)
	embed.add_field(name="Restriction", value=event.restriction, inline=True)
	embed.set_footer(text=f"CTF ID: {event.id}")
	return embed