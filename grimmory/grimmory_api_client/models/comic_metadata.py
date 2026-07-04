from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ComicMetadata")


@_attrs_define
class ComicMetadata:
    """
    Attributes:
        issue_number (str | Unset):
        volume_name (str | Unset):
        volume_number (int | Unset):
        story_arc (str | Unset):
        story_arc_number (int | Unset):
        alternate_series (str | Unset):
        alternate_issue (str | Unset):
        pencillers (list[str] | Unset):
        inkers (list[str] | Unset):
        colorists (list[str] | Unset):
        letterers (list[str] | Unset):
        cover_artists (list[str] | Unset):
        editors (list[str] | Unset):
        imprint (str | Unset):
        format_ (str | Unset):
        black_and_white (bool | Unset):
        manga (bool | Unset):
        reading_direction (str | Unset):
        characters (list[str] | Unset):
        teams (list[str] | Unset):
        locations (list[str] | Unset):
        web_link (str | Unset):
        notes (str | Unset):
        issue_number_locked (bool | Unset):
        volume_name_locked (bool | Unset):
        volume_number_locked (bool | Unset):
        story_arc_locked (bool | Unset):
        story_arc_number_locked (bool | Unset):
        alternate_series_locked (bool | Unset):
        alternate_issue_locked (bool | Unset):
        imprint_locked (bool | Unset):
        format_locked (bool | Unset):
        black_and_white_locked (bool | Unset):
        manga_locked (bool | Unset):
        reading_direction_locked (bool | Unset):
        web_link_locked (bool | Unset):
        notes_locked (bool | Unset):
        creators_locked (bool | Unset):
        pencillers_locked (bool | Unset):
        inkers_locked (bool | Unset):
        colorists_locked (bool | Unset):
        letterers_locked (bool | Unset):
        cover_artists_locked (bool | Unset):
        editors_locked (bool | Unset):
        characters_locked (bool | Unset):
        teams_locked (bool | Unset):
        locations_locked (bool | Unset):
    """

    issue_number: str | Unset = UNSET
    volume_name: str | Unset = UNSET
    volume_number: int | Unset = UNSET
    story_arc: str | Unset = UNSET
    story_arc_number: int | Unset = UNSET
    alternate_series: str | Unset = UNSET
    alternate_issue: str | Unset = UNSET
    pencillers: list[str] | Unset = UNSET
    inkers: list[str] | Unset = UNSET
    colorists: list[str] | Unset = UNSET
    letterers: list[str] | Unset = UNSET
    cover_artists: list[str] | Unset = UNSET
    editors: list[str] | Unset = UNSET
    imprint: str | Unset = UNSET
    format_: str | Unset = UNSET
    black_and_white: bool | Unset = UNSET
    manga: bool | Unset = UNSET
    reading_direction: str | Unset = UNSET
    characters: list[str] | Unset = UNSET
    teams: list[str] | Unset = UNSET
    locations: list[str] | Unset = UNSET
    web_link: str | Unset = UNSET
    notes: str | Unset = UNSET
    issue_number_locked: bool | Unset = UNSET
    volume_name_locked: bool | Unset = UNSET
    volume_number_locked: bool | Unset = UNSET
    story_arc_locked: bool | Unset = UNSET
    story_arc_number_locked: bool | Unset = UNSET
    alternate_series_locked: bool | Unset = UNSET
    alternate_issue_locked: bool | Unset = UNSET
    imprint_locked: bool | Unset = UNSET
    format_locked: bool | Unset = UNSET
    black_and_white_locked: bool | Unset = UNSET
    manga_locked: bool | Unset = UNSET
    reading_direction_locked: bool | Unset = UNSET
    web_link_locked: bool | Unset = UNSET
    notes_locked: bool | Unset = UNSET
    creators_locked: bool | Unset = UNSET
    pencillers_locked: bool | Unset = UNSET
    inkers_locked: bool | Unset = UNSET
    colorists_locked: bool | Unset = UNSET
    letterers_locked: bool | Unset = UNSET
    cover_artists_locked: bool | Unset = UNSET
    editors_locked: bool | Unset = UNSET
    characters_locked: bool | Unset = UNSET
    teams_locked: bool | Unset = UNSET
    locations_locked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issue_number = self.issue_number

        volume_name = self.volume_name

        volume_number = self.volume_number

        story_arc = self.story_arc

        story_arc_number = self.story_arc_number

        alternate_series = self.alternate_series

        alternate_issue = self.alternate_issue

        pencillers: list[str] | Unset = UNSET
        if not isinstance(self.pencillers, Unset):
            pencillers = self.pencillers

        inkers: list[str] | Unset = UNSET
        if not isinstance(self.inkers, Unset):
            inkers = self.inkers

        colorists: list[str] | Unset = UNSET
        if not isinstance(self.colorists, Unset):
            colorists = self.colorists

        letterers: list[str] | Unset = UNSET
        if not isinstance(self.letterers, Unset):
            letterers = self.letterers

        cover_artists: list[str] | Unset = UNSET
        if not isinstance(self.cover_artists, Unset):
            cover_artists = self.cover_artists

        editors: list[str] | Unset = UNSET
        if not isinstance(self.editors, Unset):
            editors = self.editors

        imprint = self.imprint

        format_ = self.format_

        black_and_white = self.black_and_white

        manga = self.manga

        reading_direction = self.reading_direction

        characters: list[str] | Unset = UNSET
        if not isinstance(self.characters, Unset):
            characters = self.characters

        teams: list[str] | Unset = UNSET
        if not isinstance(self.teams, Unset):
            teams = self.teams

        locations: list[str] | Unset = UNSET
        if not isinstance(self.locations, Unset):
            locations = self.locations

        web_link = self.web_link

        notes = self.notes

        issue_number_locked = self.issue_number_locked

        volume_name_locked = self.volume_name_locked

        volume_number_locked = self.volume_number_locked

        story_arc_locked = self.story_arc_locked

        story_arc_number_locked = self.story_arc_number_locked

        alternate_series_locked = self.alternate_series_locked

        alternate_issue_locked = self.alternate_issue_locked

        imprint_locked = self.imprint_locked

        format_locked = self.format_locked

        black_and_white_locked = self.black_and_white_locked

        manga_locked = self.manga_locked

        reading_direction_locked = self.reading_direction_locked

        web_link_locked = self.web_link_locked

        notes_locked = self.notes_locked

        creators_locked = self.creators_locked

        pencillers_locked = self.pencillers_locked

        inkers_locked = self.inkers_locked

        colorists_locked = self.colorists_locked

        letterers_locked = self.letterers_locked

        cover_artists_locked = self.cover_artists_locked

        editors_locked = self.editors_locked

        characters_locked = self.characters_locked

        teams_locked = self.teams_locked

        locations_locked = self.locations_locked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if issue_number is not UNSET:
            field_dict["issueNumber"] = issue_number
        if volume_name is not UNSET:
            field_dict["volumeName"] = volume_name
        if volume_number is not UNSET:
            field_dict["volumeNumber"] = volume_number
        if story_arc is not UNSET:
            field_dict["storyArc"] = story_arc
        if story_arc_number is not UNSET:
            field_dict["storyArcNumber"] = story_arc_number
        if alternate_series is not UNSET:
            field_dict["alternateSeries"] = alternate_series
        if alternate_issue is not UNSET:
            field_dict["alternateIssue"] = alternate_issue
        if pencillers is not UNSET:
            field_dict["pencillers"] = pencillers
        if inkers is not UNSET:
            field_dict["inkers"] = inkers
        if colorists is not UNSET:
            field_dict["colorists"] = colorists
        if letterers is not UNSET:
            field_dict["letterers"] = letterers
        if cover_artists is not UNSET:
            field_dict["coverArtists"] = cover_artists
        if editors is not UNSET:
            field_dict["editors"] = editors
        if imprint is not UNSET:
            field_dict["imprint"] = imprint
        if format_ is not UNSET:
            field_dict["format"] = format_
        if black_and_white is not UNSET:
            field_dict["blackAndWhite"] = black_and_white
        if manga is not UNSET:
            field_dict["manga"] = manga
        if reading_direction is not UNSET:
            field_dict["readingDirection"] = reading_direction
        if characters is not UNSET:
            field_dict["characters"] = characters
        if teams is not UNSET:
            field_dict["teams"] = teams
        if locations is not UNSET:
            field_dict["locations"] = locations
        if web_link is not UNSET:
            field_dict["webLink"] = web_link
        if notes is not UNSET:
            field_dict["notes"] = notes
        if issue_number_locked is not UNSET:
            field_dict["issueNumberLocked"] = issue_number_locked
        if volume_name_locked is not UNSET:
            field_dict["volumeNameLocked"] = volume_name_locked
        if volume_number_locked is not UNSET:
            field_dict["volumeNumberLocked"] = volume_number_locked
        if story_arc_locked is not UNSET:
            field_dict["storyArcLocked"] = story_arc_locked
        if story_arc_number_locked is not UNSET:
            field_dict["storyArcNumberLocked"] = story_arc_number_locked
        if alternate_series_locked is not UNSET:
            field_dict["alternateSeriesLocked"] = alternate_series_locked
        if alternate_issue_locked is not UNSET:
            field_dict["alternateIssueLocked"] = alternate_issue_locked
        if imprint_locked is not UNSET:
            field_dict["imprintLocked"] = imprint_locked
        if format_locked is not UNSET:
            field_dict["formatLocked"] = format_locked
        if black_and_white_locked is not UNSET:
            field_dict["blackAndWhiteLocked"] = black_and_white_locked
        if manga_locked is not UNSET:
            field_dict["mangaLocked"] = manga_locked
        if reading_direction_locked is not UNSET:
            field_dict["readingDirectionLocked"] = reading_direction_locked
        if web_link_locked is not UNSET:
            field_dict["webLinkLocked"] = web_link_locked
        if notes_locked is not UNSET:
            field_dict["notesLocked"] = notes_locked
        if creators_locked is not UNSET:
            field_dict["creatorsLocked"] = creators_locked
        if pencillers_locked is not UNSET:
            field_dict["pencillersLocked"] = pencillers_locked
        if inkers_locked is not UNSET:
            field_dict["inkersLocked"] = inkers_locked
        if colorists_locked is not UNSET:
            field_dict["coloristsLocked"] = colorists_locked
        if letterers_locked is not UNSET:
            field_dict["letterersLocked"] = letterers_locked
        if cover_artists_locked is not UNSET:
            field_dict["coverArtistsLocked"] = cover_artists_locked
        if editors_locked is not UNSET:
            field_dict["editorsLocked"] = editors_locked
        if characters_locked is not UNSET:
            field_dict["charactersLocked"] = characters_locked
        if teams_locked is not UNSET:
            field_dict["teamsLocked"] = teams_locked
        if locations_locked is not UNSET:
            field_dict["locationsLocked"] = locations_locked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        issue_number = d.pop("issueNumber", UNSET)

        volume_name = d.pop("volumeName", UNSET)

        volume_number = d.pop("volumeNumber", UNSET)

        story_arc = d.pop("storyArc", UNSET)

        story_arc_number = d.pop("storyArcNumber", UNSET)

        alternate_series = d.pop("alternateSeries", UNSET)

        alternate_issue = d.pop("alternateIssue", UNSET)

        pencillers = cast(list[str], d.pop("pencillers", UNSET))

        inkers = cast(list[str], d.pop("inkers", UNSET))

        colorists = cast(list[str], d.pop("colorists", UNSET))

        letterers = cast(list[str], d.pop("letterers", UNSET))

        cover_artists = cast(list[str], d.pop("coverArtists", UNSET))

        editors = cast(list[str], d.pop("editors", UNSET))

        imprint = d.pop("imprint", UNSET)

        format_ = d.pop("format", UNSET)

        black_and_white = d.pop("blackAndWhite", UNSET)

        manga = d.pop("manga", UNSET)

        reading_direction = d.pop("readingDirection", UNSET)

        characters = cast(list[str], d.pop("characters", UNSET))

        teams = cast(list[str], d.pop("teams", UNSET))

        locations = cast(list[str], d.pop("locations", UNSET))

        web_link = d.pop("webLink", UNSET)

        notes = d.pop("notes", UNSET)

        issue_number_locked = d.pop("issueNumberLocked", UNSET)

        volume_name_locked = d.pop("volumeNameLocked", UNSET)

        volume_number_locked = d.pop("volumeNumberLocked", UNSET)

        story_arc_locked = d.pop("storyArcLocked", UNSET)

        story_arc_number_locked = d.pop("storyArcNumberLocked", UNSET)

        alternate_series_locked = d.pop("alternateSeriesLocked", UNSET)

        alternate_issue_locked = d.pop("alternateIssueLocked", UNSET)

        imprint_locked = d.pop("imprintLocked", UNSET)

        format_locked = d.pop("formatLocked", UNSET)

        black_and_white_locked = d.pop("blackAndWhiteLocked", UNSET)

        manga_locked = d.pop("mangaLocked", UNSET)

        reading_direction_locked = d.pop("readingDirectionLocked", UNSET)

        web_link_locked = d.pop("webLinkLocked", UNSET)

        notes_locked = d.pop("notesLocked", UNSET)

        creators_locked = d.pop("creatorsLocked", UNSET)

        pencillers_locked = d.pop("pencillersLocked", UNSET)

        inkers_locked = d.pop("inkersLocked", UNSET)

        colorists_locked = d.pop("coloristsLocked", UNSET)

        letterers_locked = d.pop("letterersLocked", UNSET)

        cover_artists_locked = d.pop("coverArtistsLocked", UNSET)

        editors_locked = d.pop("editorsLocked", UNSET)

        characters_locked = d.pop("charactersLocked", UNSET)

        teams_locked = d.pop("teamsLocked", UNSET)

        locations_locked = d.pop("locationsLocked", UNSET)

        comic_metadata = cls(
            issue_number=issue_number,
            volume_name=volume_name,
            volume_number=volume_number,
            story_arc=story_arc,
            story_arc_number=story_arc_number,
            alternate_series=alternate_series,
            alternate_issue=alternate_issue,
            pencillers=pencillers,
            inkers=inkers,
            colorists=colorists,
            letterers=letterers,
            cover_artists=cover_artists,
            editors=editors,
            imprint=imprint,
            format_=format_,
            black_and_white=black_and_white,
            manga=manga,
            reading_direction=reading_direction,
            characters=characters,
            teams=teams,
            locations=locations,
            web_link=web_link,
            notes=notes,
            issue_number_locked=issue_number_locked,
            volume_name_locked=volume_name_locked,
            volume_number_locked=volume_number_locked,
            story_arc_locked=story_arc_locked,
            story_arc_number_locked=story_arc_number_locked,
            alternate_series_locked=alternate_series_locked,
            alternate_issue_locked=alternate_issue_locked,
            imprint_locked=imprint_locked,
            format_locked=format_locked,
            black_and_white_locked=black_and_white_locked,
            manga_locked=manga_locked,
            reading_direction_locked=reading_direction_locked,
            web_link_locked=web_link_locked,
            notes_locked=notes_locked,
            creators_locked=creators_locked,
            pencillers_locked=pencillers_locked,
            inkers_locked=inkers_locked,
            colorists_locked=colorists_locked,
            letterers_locked=letterers_locked,
            cover_artists_locked=cover_artists_locked,
            editors_locked=editors_locked,
            characters_locked=characters_locked,
            teams_locked=teams_locked,
            locations_locked=locations_locked,
        )

        comic_metadata.additional_properties = d
        return comic_metadata

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
