from .table import TableRow

class SchemaMigrationsRow(TableRow):
	def __init__(self):
		super().__init__('schema_migrations')
		self._version = None
		self._dirty = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def version(self):
		return self._version

	@version.setter
	def version(self, version):
		self._version = version

	@property
	def dirty(self):
		return self._dirty

	@dirty.setter
	def dirty(self, dirty):
		self._dirty = dirty

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.version, self.dirty]
		else:
			return [self.version, self.dirty]

class TagsRow(TableRow):
	def __init__(self):
		super().__init__('tags')
		self._id = None
		self._name = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.name, self.created_at, self.updated_at]
		else:
			return [self.name, self.created_at, self.updated_at]

class SqliteSequenceRow(TableRow):
	def __init__(self):
		super().__init__('sqlite_sequence')
		self._name = None
		self._seq = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def seq(self):
		return self._seq

	@seq.setter
	def seq(self, seq):
		self._seq = seq

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.name, self.seq]
		else:
			return [self.name, self.seq]

class StudiosRow(TableRow):
	def __init__(self):
		super().__init__('studios')
		self._id = None
		self._checksum = None
		self._name = None
		self._url = None
		self._parent_id = None
		self._created_at = None
		self._updated_at = None
		self._details = None
		self._rating = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def checksum(self):
		return self._checksum

	@checksum.setter
	def checksum(self, checksum):
		self._checksum = checksum

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def parent_id(self):
		return self._parent_id

	@parent_id.setter
	def parent_id(self, parent_id):
		self._parent_id = parent_id

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	@property
	def details(self):
		return self._details

	@details.setter
	def details(self, details):
		self._details = details

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.checksum, self.name, self.url, self.parent_id, self.created_at, self.updated_at, self.details, self.rating]
		else:
			return [self.checksum, self.name, self.url, self.parent_id, self.created_at, self.updated_at, self.details, self.rating]

class PerformersRow(TableRow):
	def __init__(self):
		super().__init__('performers')
		self._id = None
		self._checksum = None
		self._name = None
		self._gender = None
		self._url = None
		self._twitter = None
		self._instagram = None
		self._birthdate = None
		self._ethnicity = None
		self._country = None
		self._eye_color = None
		self._height = None
		self._measurements = None
		self._fake_tits = None
		self._career_length = None
		self._tattoos = None
		self._piercings = None
		self._aliases = None
		self._favorite = None
		self._created_at = None
		self._updated_at = None
		self._details = None
		self._death_date = None
		self._hair_color = None
		self._weight = None
		self._rating = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def checksum(self):
		return self._checksum

	@checksum.setter
	def checksum(self, checksum):
		self._checksum = checksum

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def gender(self):
		return self._gender

	@gender.setter
	def gender(self, gender):
		self._gender = gender

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def twitter(self):
		return self._twitter

	@twitter.setter
	def twitter(self, twitter):
		self._twitter = twitter

	@property
	def instagram(self):
		return self._instagram

	@instagram.setter
	def instagram(self, instagram):
		self._instagram = instagram

	@property
	def birthdate(self):
		return self._birthdate

	@birthdate.setter
	def birthdate(self, birthdate):
		self._birthdate = birthdate

	@property
	def ethnicity(self):
		return self._ethnicity

	@ethnicity.setter
	def ethnicity(self, ethnicity):
		self._ethnicity = ethnicity

	@property
	def country(self):
		return self._country

	@country.setter
	def country(self, country):
		self._country = country

	@property
	def eye_color(self):
		return self._eye_color

	@eye_color.setter
	def eye_color(self, eye_color):
		self._eye_color = eye_color

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height

	@property
	def measurements(self):
		return self._measurements

	@measurements.setter
	def measurements(self, measurements):
		self._measurements = measurements

	@property
	def fake_tits(self):
		return self._fake_tits

	@fake_tits.setter
	def fake_tits(self, fake_tits):
		self._fake_tits = fake_tits

	@property
	def career_length(self):
		return self._career_length

	@career_length.setter
	def career_length(self, career_length):
		self._career_length = career_length

	@property
	def tattoos(self):
		return self._tattoos

	@tattoos.setter
	def tattoos(self, tattoos):
		self._tattoos = tattoos

	@property
	def piercings(self):
		return self._piercings

	@piercings.setter
	def piercings(self, piercings):
		self._piercings = piercings

	@property
	def aliases(self):
		return self._aliases

	@aliases.setter
	def aliases(self, aliases):
		self._aliases = aliases

	@property
	def favorite(self):
		return self._favorite

	@favorite.setter
	def favorite(self, favorite):
		self._favorite = favorite

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	@property
	def details(self):
		return self._details

	@details.setter
	def details(self, details):
		self._details = details

	@property
	def death_date(self):
		return self._death_date

	@death_date.setter
	def death_date(self, death_date):
		self._death_date = death_date

	@property
	def hair_color(self):
		return self._hair_color

	@hair_color.setter
	def hair_color(self, hair_color):
		self._hair_color = hair_color

	@property
	def weight(self):
		return self._weight

	@weight.setter
	def weight(self, weight):
		self._weight = weight

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.checksum, self.name, self.gender, self.url, self.twitter, self.instagram, self.birthdate, self.ethnicity, self.country, self.eye_color, self.height, self.measurements, self.fake_tits, self.career_length, self.tattoos, self.piercings, self.aliases, self.favorite, self.created_at, self.updated_at, self.details, self.death_date, self.hair_color, self.weight, self.rating]
		else:
			return [self.checksum, self.name, self.gender, self.url, self.twitter, self.instagram, self.birthdate, self.ethnicity, self.country, self.eye_color, self.height, self.measurements, self.fake_tits, self.career_length, self.tattoos, self.piercings, self.aliases, self.favorite, self.created_at, self.updated_at, self.details, self.death_date, self.hair_color, self.weight, self.rating]

class MoviesRow(TableRow):
	def __init__(self):
		super().__init__('movies')
		self._id = None
		self._name = None
		self._aliases = None
		self._duration = None
		self._date = None
		self._rating = None
		self._studio_id = None
		self._director = None
		self._synopsis = None
		self._checksum = None
		self._url = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def aliases(self):
		return self._aliases

	@aliases.setter
	def aliases(self, aliases):
		self._aliases = aliases

	@property
	def duration(self):
		return self._duration

	@duration.setter
	def duration(self, duration):
		self._duration = duration

	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, date):
		self._date = date

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def director(self):
		return self._director

	@director.setter
	def director(self, director):
		self._director = director

	@property
	def synopsis(self):
		return self._synopsis

	@synopsis.setter
	def synopsis(self, synopsis):
		self._synopsis = synopsis

	@property
	def checksum(self):
		return self._checksum

	@checksum.setter
	def checksum(self, checksum):
		self._checksum = checksum

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.name, self.aliases, self.duration, self.date, self.rating, self.studio_id, self.director, self.synopsis, self.checksum, self.url, self.created_at, self.updated_at]
		else:
			return [self.name, self.aliases, self.duration, self.date, self.rating, self.studio_id, self.director, self.synopsis, self.checksum, self.url, self.created_at, self.updated_at]

class ScrapedItemsRow(TableRow):
	def __init__(self):
		super().__init__('scraped_items')
		self._id = None
		self._title = None
		self._description = None
		self._url = None
		self._date = None
		self._rating = None
		self._tags = None
		self._models = None
		self._episode = None
		self._gallery_filename = None
		self._gallery_url = None
		self._video_filename = None
		self._video_url = None
		self._studio_id = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def description(self):
		return self._description

	@description.setter
	def description(self, description):
		self._description = description

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, date):
		self._date = date

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def tags(self):
		return self._tags

	@tags.setter
	def tags(self, tags):
		self._tags = tags

	@property
	def models(self):
		return self._models

	@models.setter
	def models(self, models):
		self._models = models

	@property
	def episode(self):
		return self._episode

	@episode.setter
	def episode(self, episode):
		self._episode = episode

	@property
	def gallery_filename(self):
		return self._gallery_filename

	@gallery_filename.setter
	def gallery_filename(self, gallery_filename):
		self._gallery_filename = gallery_filename

	@property
	def gallery_url(self):
		return self._gallery_url

	@gallery_url.setter
	def gallery_url(self, gallery_url):
		self._gallery_url = gallery_url

	@property
	def video_filename(self):
		return self._video_filename

	@video_filename.setter
	def video_filename(self, video_filename):
		self._video_filename = video_filename

	@property
	def video_url(self):
		return self._video_url

	@video_url.setter
	def video_url(self, video_url):
		self._video_url = video_url

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.title, self.description, self.url, self.date, self.rating, self.tags, self.models, self.episode, self.gallery_filename, self.gallery_url, self.video_filename, self.video_url, self.studio_id, self.created_at, self.updated_at]
		else:
			return [self.title, self.description, self.url, self.date, self.rating, self.tags, self.models, self.episode, self.gallery_filename, self.gallery_url, self.video_filename, self.video_url, self.studio_id, self.created_at, self.updated_at]

class PerformersImageRow(TableRow):
	def __init__(self):
		super().__init__('performers_image')
		self._performer_id = None
		self._image = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, image):
		self._image = image

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.image]
		else:
			return [self.performer_id, self.image]

class StudiosImageRow(TableRow):
	def __init__(self):
		super().__init__('studios_image')
		self._studio_id = None
		self._image = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, image):
		self._image = image

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.studio_id, self.image]
		else:
			return [self.studio_id, self.image]

class MoviesImagesRow(TableRow):
	def __init__(self):
		super().__init__('movies_images')
		self._movie_id = None
		self._front_image = None
		self._back_image = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def movie_id(self):
		return self._movie_id

	@movie_id.setter
	def movie_id(self, movie_id):
		self._movie_id = movie_id

	@property
	def front_image(self):
		return self._front_image

	@front_image.setter
	def front_image(self, front_image):
		self._front_image = front_image

	@property
	def back_image(self):
		return self._back_image

	@back_image.setter
	def back_image(self, back_image):
		self._back_image = back_image

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.movie_id, self.front_image, self.back_image]
		else:
			return [self.movie_id, self.front_image, self.back_image]

class TagsImageRow(TableRow):
	def __init__(self):
		super().__init__('tags_image')
		self._tag_id = None
		self._image = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	@property
	def image(self):
		return self._image

	@image.setter
	def image(self, image):
		self._image = image

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.tag_id, self.image]
		else:
			return [self.tag_id, self.image]

class ScenesRow(TableRow):
	def __init__(self):
		super().__init__('scenes')
		self._id = None
		self._path = None
		self._checksum = None
		self._oshash = None
		self._title = None
		self._details = None
		self._url = None
		self._date = None
		self._rating = None
		self._size = None
		self._duration = None
		self._video_codec = None
		self._audio_codec = None
		self._width = None
		self._height = None
		self._framerate = None
		self._bitrate = None
		self._studio_id = None
		self._o_counter = None
		self._format = None
		self._created_at = None
		self._updated_at = None
		self._file_mod_time = None
		self._organized = None
		self._phash = None
		self._interactive = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def checksum(self):
		return self._checksum

	@checksum.setter
	def checksum(self, checksum):
		self._checksum = checksum

	@property
	def oshash(self):
		return self._oshash

	@oshash.setter
	def oshash(self, oshash):
		self._oshash = oshash

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def details(self):
		return self._details

	@details.setter
	def details(self, details):
		self._details = details

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, date):
		self._date = date

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, size):
		self._size = size

	@property
	def duration(self):
		return self._duration

	@duration.setter
	def duration(self, duration):
		self._duration = duration

	@property
	def video_codec(self):
		return self._video_codec

	@video_codec.setter
	def video_codec(self, video_codec):
		self._video_codec = video_codec

	@property
	def audio_codec(self):
		return self._audio_codec

	@audio_codec.setter
	def audio_codec(self, audio_codec):
		self._audio_codec = audio_codec

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height

	@property
	def framerate(self):
		return self._framerate

	@framerate.setter
	def framerate(self, framerate):
		self._framerate = framerate

	@property
	def bitrate(self):
		return self._bitrate

	@bitrate.setter
	def bitrate(self, bitrate):
		self._bitrate = bitrate

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def o_counter(self):
		return self._o_counter

	@o_counter.setter
	def o_counter(self, o_counter):
		self._o_counter = o_counter

	@property
	def format(self):
		return self._format

	@format.setter
	def format(self, format):
		self._format = format

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	@property
	def file_mod_time(self):
		return self._file_mod_time

	@file_mod_time.setter
	def file_mod_time(self, file_mod_time):
		self._file_mod_time = file_mod_time

	@property
	def organized(self):
		return self._organized

	@organized.setter
	def organized(self, organized):
		self._organized = organized

	@property
	def phash(self):
		return self._phash

	@phash.setter
	def phash(self, phash):
		self._phash = phash

	@property
	def interactive(self):
		return self._interactive

	@interactive.setter
	def interactive(self, interactive):
		self._interactive = interactive

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.path, self.checksum, self.oshash, self.title, self.details, self.url, self.date, self.rating, self.size, self.duration, self.video_codec, self.audio_codec, self.width, self.height, self.framerate, self.bitrate, self.studio_id, self.o_counter, self.format, self.created_at, self.updated_at, self.file_mod_time, self.organized, self.phash, self.interactive]
		else:
			return [self.path, self.checksum, self.oshash, self.title, self.details, self.url, self.date, self.rating, self.size, self.duration, self.video_codec, self.audio_codec, self.width, self.height, self.framerate, self.bitrate, self.studio_id, self.o_counter, self.format, self.created_at, self.updated_at, self.file_mod_time, self.organized, self.phash, self.interactive]

class PerformersScenesRow(TableRow):
	def __init__(self):
		super().__init__('performers_scenes')
		self._performer_id = None
		self._scene_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.scene_id]
		else:
			return [self.performer_id, self.scene_id]

class SceneMarkersRow(TableRow):
	def __init__(self):
		super().__init__('scene_markers')
		self._id = None
		self._title = None
		self._seconds = None
		self._primary_tag_id = None
		self._scene_id = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def seconds(self):
		return self._seconds

	@seconds.setter
	def seconds(self, seconds):
		self._seconds = seconds

	@property
	def primary_tag_id(self):
		return self._primary_tag_id

	@primary_tag_id.setter
	def primary_tag_id(self, primary_tag_id):
		self._primary_tag_id = primary_tag_id

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.title, self.seconds, self.primary_tag_id, self.scene_id, self.created_at, self.updated_at]
		else:
			return [self.title, self.seconds, self.primary_tag_id, self.scene_id, self.created_at, self.updated_at]

class SceneMarkersTagsRow(TableRow):
	def __init__(self):
		super().__init__('scene_markers_tags')
		self._scene_marker_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_marker_id(self):
		return self._scene_marker_id

	@scene_marker_id.setter
	def scene_marker_id(self, scene_marker_id):
		self._scene_marker_id = scene_marker_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_marker_id, self.tag_id]
		else:
			return [self.scene_marker_id, self.tag_id]

class ScenesTagsRow(TableRow):
	def __init__(self):
		super().__init__('scenes_tags')
		self._scene_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_id, self.tag_id]
		else:
			return [self.scene_id, self.tag_id]

class MoviesScenesRow(TableRow):
	def __init__(self):
		super().__init__('movies_scenes')
		self._movie_id = None
		self._scene_id = None
		self._scene_index = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def movie_id(self):
		return self._movie_id

	@movie_id.setter
	def movie_id(self, movie_id):
		self._movie_id = movie_id

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def scene_index(self):
		return self._scene_index

	@scene_index.setter
	def scene_index(self, scene_index):
		self._scene_index = scene_index

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.movie_id, self.scene_id, self.scene_index]
		else:
			return [self.movie_id, self.scene_id, self.scene_index]

class ScenesCoverRow(TableRow):
	def __init__(self):
		super().__init__('scenes_cover')
		self._scene_id = None
		self._cover = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def cover(self):
		return self._cover

	@cover.setter
	def cover(self, cover):
		self._cover = cover

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_id, self.cover]
		else:
			return [self.scene_id, self.cover]

class ImagesRow(TableRow):
	def __init__(self):
		super().__init__('images')
		self._id = None
		self._path = None
		self._checksum = None
		self._title = None
		self._rating = None
		self._size = None
		self._width = None
		self._height = None
		self._studio_id = None
		self._o_counter = None
		self._created_at = None
		self._updated_at = None
		self._file_mod_time = None
		self._organized = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def checksum(self):
		return self._checksum

	@checksum.setter
	def checksum(self, checksum):
		self._checksum = checksum

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, size):
		self._size = size

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		self._height = height

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def o_counter(self):
		return self._o_counter

	@o_counter.setter
	def o_counter(self, o_counter):
		self._o_counter = o_counter

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	@property
	def file_mod_time(self):
		return self._file_mod_time

	@file_mod_time.setter
	def file_mod_time(self, file_mod_time):
		self._file_mod_time = file_mod_time

	@property
	def organized(self):
		return self._organized

	@organized.setter
	def organized(self, organized):
		self._organized = organized

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.path, self.checksum, self.title, self.rating, self.size, self.width, self.height, self.studio_id, self.o_counter, self.created_at, self.updated_at, self.file_mod_time, self.organized]
		else:
			return [self.path, self.checksum, self.title, self.rating, self.size, self.width, self.height, self.studio_id, self.o_counter, self.created_at, self.updated_at, self.file_mod_time, self.organized]

class PerformersImagesRow(TableRow):
	def __init__(self):
		super().__init__('performers_images')
		self._performer_id = None
		self._image_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def image_id(self):
		return self._image_id

	@image_id.setter
	def image_id(self, image_id):
		self._image_id = image_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.image_id]
		else:
			return [self.performer_id, self.image_id]

class ImagesTagsRow(TableRow):
	def __init__(self):
		super().__init__('images_tags')
		self._image_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def image_id(self):
		return self._image_id

	@image_id.setter
	def image_id(self, image_id):
		self._image_id = image_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.image_id, self.tag_id]
		else:
			return [self.image_id, self.tag_id]

class SceneStashIdsRow(TableRow):
	def __init__(self):
		super().__init__('scene_stash_ids')
		self._scene_id = None
		self._endpoint = None
		self._stash_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def endpoint(self):
		return self._endpoint

	@endpoint.setter
	def endpoint(self, endpoint):
		self._endpoint = endpoint

	@property
	def stash_id(self):
		return self._stash_id

	@stash_id.setter
	def stash_id(self, stash_id):
		self._stash_id = stash_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_id, self.endpoint, self.stash_id]
		else:
			return [self.scene_id, self.endpoint, self.stash_id]

class PerformerStashIdsRow(TableRow):
	def __init__(self):
		super().__init__('performer_stash_ids')
		self._performer_id = None
		self._endpoint = None
		self._stash_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def endpoint(self):
		return self._endpoint

	@endpoint.setter
	def endpoint(self, endpoint):
		self._endpoint = endpoint

	@property
	def stash_id(self):
		return self._stash_id

	@stash_id.setter
	def stash_id(self, stash_id):
		self._stash_id = stash_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.endpoint, self.stash_id]
		else:
			return [self.performer_id, self.endpoint, self.stash_id]

class StudioStashIdsRow(TableRow):
	def __init__(self):
		super().__init__('studio_stash_ids')
		self._studio_id = None
		self._endpoint = None
		self._stash_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def endpoint(self):
		return self._endpoint

	@endpoint.setter
	def endpoint(self, endpoint):
		self._endpoint = endpoint

	@property
	def stash_id(self):
		return self._stash_id

	@stash_id.setter
	def stash_id(self, stash_id):
		self._stash_id = stash_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.studio_id, self.endpoint, self.stash_id]
		else:
			return [self.studio_id, self.endpoint, self.stash_id]

class GalleriesRow(TableRow):
	def __init__(self):
		super().__init__('galleries')
		self._id = None
		self._path = None
		self._checksum = None
		self._zip = None
		self._title = None
		self._url = None
		self._date = None
		self._details = None
		self._studio_id = None
		self._rating = None
		self._file_mod_time = None
		self._organized = None
		self._created_at = None
		self._updated_at = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def path(self):
		return self._path

	@path.setter
	def path(self, path):
		self._path = path

	@property
	def checksum(self):
		return self._checksum

	@checksum.setter
	def checksum(self, checksum):
		self._checksum = checksum

	@property
	def zip(self):
		return self._zip

	@zip.setter
	def zip(self, zip):
		self._zip = zip

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, title):
		self._title = title

	@property
	def url(self):
		return self._url

	@url.setter
	def url(self, url):
		self._url = url

	@property
	def date(self):
		return self._date

	@date.setter
	def date(self, date):
		self._date = date

	@property
	def details(self):
		return self._details

	@details.setter
	def details(self, details):
		self._details = details

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def rating(self):
		return self._rating

	@rating.setter
	def rating(self, rating):
		self._rating = rating

	@property
	def file_mod_time(self):
		return self._file_mod_time

	@file_mod_time.setter
	def file_mod_time(self, file_mod_time):
		self._file_mod_time = file_mod_time

	@property
	def organized(self):
		return self._organized

	@organized.setter
	def organized(self, organized):
		self._organized = organized

	@property
	def created_at(self):
		return self._created_at

	@created_at.setter
	def created_at(self, created_at):
		self._created_at = created_at

	@property
	def updated_at(self):
		return self._updated_at

	@updated_at.setter
	def updated_at(self, updated_at):
		self._updated_at = updated_at

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.path, self.checksum, self.zip, self.title, self.url, self.date, self.details, self.studio_id, self.rating, self.file_mod_time, self.organized, self.created_at, self.updated_at]
		else:
			return [self.path, self.checksum, self.zip, self.title, self.url, self.date, self.details, self.studio_id, self.rating, self.file_mod_time, self.organized, self.created_at, self.updated_at]

class ScenesGalleriesRow(TableRow):
	def __init__(self):
		super().__init__('scenes_galleries')
		self._scene_id = None
		self._gallery_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def scene_id(self):
		return self._scene_id

	@scene_id.setter
	def scene_id(self, scene_id):
		self._scene_id = scene_id

	@property
	def gallery_id(self):
		return self._gallery_id

	@gallery_id.setter
	def gallery_id(self, gallery_id):
		self._gallery_id = gallery_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.scene_id, self.gallery_id]
		else:
			return [self.scene_id, self.gallery_id]

class GalleriesImagesRow(TableRow):
	def __init__(self):
		super().__init__('galleries_images')
		self._gallery_id = None
		self._image_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def gallery_id(self):
		return self._gallery_id

	@gallery_id.setter
	def gallery_id(self, gallery_id):
		self._gallery_id = gallery_id

	@property
	def image_id(self):
		return self._image_id

	@image_id.setter
	def image_id(self, image_id):
		self._image_id = image_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.gallery_id, self.image_id]
		else:
			return [self.gallery_id, self.image_id]

class PerformersGalleriesRow(TableRow):
	def __init__(self):
		super().__init__('performers_galleries')
		self._performer_id = None
		self._gallery_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def gallery_id(self):
		return self._gallery_id

	@gallery_id.setter
	def gallery_id(self, gallery_id):
		self._gallery_id = gallery_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.gallery_id]
		else:
			return [self.performer_id, self.gallery_id]

class GalleriesTagsRow(TableRow):
	def __init__(self):
		super().__init__('galleries_tags')
		self._gallery_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def gallery_id(self):
		return self._gallery_id

	@gallery_id.setter
	def gallery_id(self, gallery_id):
		self._gallery_id = gallery_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.gallery_id, self.tag_id]
		else:
			return [self.gallery_id, self.tag_id]

class PerformersTagsRow(TableRow):
	def __init__(self):
		super().__init__('performers_tags')
		self._performer_id = None
		self._tag_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def performer_id(self):
		return self._performer_id

	@performer_id.setter
	def performer_id(self, performer_id):
		self._performer_id = performer_id

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.performer_id, self.tag_id]
		else:
			return [self.performer_id, self.tag_id]

class TagAliasesRow(TableRow):
	def __init__(self):
		super().__init__('tag_aliases')
		self._tag_id = None
		self._alias = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def tag_id(self):
		return self._tag_id

	@tag_id.setter
	def tag_id(self, tag_id):
		self._tag_id = tag_id

	@property
	def alias(self):
		return self._alias

	@alias.setter
	def alias(self, alias):
		self._alias = alias

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.tag_id, self.alias]
		else:
			return [self.tag_id, self.alias]

class SavedFiltersRow(TableRow):
	def __init__(self):
		super().__init__('saved_filters')
		self._id = None
		self._name = None
		self._mode = None
		self._filter = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def id(self):
		return self._id

	@id.setter
	def id(self, id):
		self._id = id

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, name):
		self._name = name

	@property
	def mode(self):
		return self._mode

	@mode.setter
	def mode(self, mode):
		self._mode = mode

	@property
	def filter(self):
		return self._filter

	@filter.setter
	def filter(self, filter):
		self._filter = filter

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.id, self.name, self.mode, self.filter]
		else:
			return [self.name, self.mode, self.filter]

class TagsRelationsRow(TableRow):
	def __init__(self):
		super().__init__('tags_relations')
		self._parent_id = None
		self._child_id = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def parent_id(self):
		return self._parent_id

	@parent_id.setter
	def parent_id(self, parent_id):
		self._parent_id = parent_id

	@property
	def child_id(self):
		return self._child_id

	@child_id.setter
	def child_id(self, child_id):
		self._child_id = child_id

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.parent_id, self.child_id]
		else:
			return [self.parent_id, self.child_id]

class StudioAliasesRow(TableRow):
	def __init__(self):
		super().__init__('studio_aliases')
		self._studio_id = None
		self._alias = None

	@property
	def table_name(self):
		return self._table_name

	@property
	def studio_id(self):
		return self._studio_id

	@studio_id.setter
	def studio_id(self, studio_id):
		self._studio_id = studio_id

	@property
	def alias(self):
		return self._alias

	@alias.setter
	def alias(self, alias):
		self._alias = alias

	def __str__(self):
		return str(self.__class__) + ": " + str(self.__dict__)

	def values_list(self, include_id=False):
		if include_id:
			return [self.studio_id, self.alias]
		else:
			return [self.studio_id, self.alias]
