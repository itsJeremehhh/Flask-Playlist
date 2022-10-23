"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlist"

    playlist = db.Column(
        db.string(),
        nullable=False,
        unique=True,
        primary_key=True
    )


class Song(db.Model):
    """Song."""

    # ADD THE NECESSARY CODE HERE
__tablename__ = "song"

song = db.Column(
    db.string()
    nullable=False,
    unique=True,
    primary_key=True

)

class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    # ADD THE NECESSARY CODE HERE
    __tablename__ = "playlist_songs"

    playlist_song = db.Column(
        db.string(),
        nullable=False,
        unique=True,

    )


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
