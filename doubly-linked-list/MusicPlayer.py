# MusicPlayer Song (Node)
class Song:
    def __init__(self, title, artist, duration, next=None, prev=None):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = next
        self.prev = prev

    def get_next(self):
        return self.next
    
    def set_next(self, song):
        self.next = song
    
    def get_prev(self):
        return self.prev
    
    def set_prev(self, song):
        self.prev = song

    def get_title(self):
        return self.title
    
    def set_title(self, title):
        self.title = title
    
    def get_artist(self):
        return self.artist
    
    def set_artit(self, artist):
        self.artist = artist
    
    def get_duration(self):
        return self.duration
    
    def set_duration(self, duration):
        self.duration = duration
    
    def get_all_info(self):
        return self.title, self.artist, self.duration
    
    def set_all_info(self, title, artist='Unknown', duration='0:00'):
        self.title = title
        self.artist = artist
        self.duration = duration
    
    def has_next(self):
        return self.next != None

# Main MusicPlayer to Hold Songs (Doubly Linked List)
class MusicPlayer:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.current_song = None
    
    def play(self):
        # Play current song. If None, play head.
        if not self.current_song:
            self.current_song = self.head
        if self.current_song:
            print('Playing > {}'.format(
                self.current_song.get_title()))
        else:
            print('No songs in library.')
    
    def next(self):
        # Play next song. If at end, play head.
        if self.current_song:
            next = self.current_song.get_next()
            if not next:
                self.current_song = self.head
            else:
                self.current_song = next
        self.play()
    
    def prev(self):
        # Play previous song. If at beginning, play tail.
        if self.current_song:
            prev = self.current_song.get_prev()
            if not prev:
                self.current_song = self.tail
            else:
                self.current_song = prev
        self.play()
    
    def get_current_song(self):
        return self.current_song
    
    def get_size(self):
        return self.size
    
    def add(self, title, artist='Unknown', duration='0:00'):
        # Create new song with next pointer set to MusicPlayer head,
        #   and previous pointer set to None. Set new song as head.
        new_song = Song(title, artist, duration, self.head)
        if self.head:
            self.head.set_prev(new_song)
        else:
            self.tail = new_song
        self.head = new_song
        self.size += 1

    def remove(self, title, partial_match=True):
        # Set variable for iteration.
        this_song = self.head
        # 
        # Iterate until end of MusicPlayer, or target song is found
        while this_song is not None:
            # 
            # Check if target title matches this song's title.
            is_match = self._is_match(
                title, this_song.get_title(), partial_match)
            # 
            # If target has been found, set next pointer of previous
            #   song to next song, and set previous pointer of next song
            #   to previous song (which deletes this song). Decrement
            #   library size.
            if is_match:
                next = this_song.get_next()
                prev = this_song.get_prev()
                # 
                if next:
                    next.set_prev(prev)
                else:
                    self.tail = prev
                # 
                if prev:
                    prev.set_next(next)
                else:
                    self.head = next
                # 
                self.size -= 1
                # 
                # Set current song if necessary.
                if self.current_song == this_song:
                    self.current_song = None

                # Song successfully removed.
                return True
            # 
            # If not found, set variable for next iteration.
            else:
                this_song = this_song.get_next()
        # 
        # Song not found.
        return False

    def _is_match(self, target_title, item_title,
    partial_match=True):
        # Check if target title is part of the item title
        #   (partial_match=True, default).
        if partial_match:
            return target_title in item_title
        # 
        # OR, check if target title completely matches item
        #   title (partial_match=False)
        return target_title == item_title
    
    def __repr__(self):
        # Combine MusicPlayer song titles, artists, and durations into
        #   string for display.
        this_song = self.head
        list_string = 'SONG LIBRARY:\n'
        while this_song != None:
            title, artist, duration = this_song.get_all_info()
            song_string = '{0} | {1} | {2}\n'.format(
                title, artist, duration)
            list_string += song_string
            this_song = this_song.get_next()
        return list_string
