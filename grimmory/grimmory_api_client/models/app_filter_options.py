from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.counted_option import CountedOption
    from ..models.language_option import LanguageOption


T = TypeVar("T", bound="AppFilterOptions")


@_attrs_define
class AppFilterOptions:
    """
    Attributes:
        authors (list[CountedOption] | Unset):
        languages (list[LanguageOption] | Unset):
        read_statuses (list[CountedOption] | Unset):
        file_types (list[CountedOption] | Unset):
        categories (list[CountedOption] | Unset):
        publishers (list[CountedOption] | Unset):
        series (list[CountedOption] | Unset):
        tags (list[CountedOption] | Unset):
        moods (list[CountedOption] | Unset):
        narrators (list[CountedOption] | Unset):
        age_ratings (list[CountedOption] | Unset):
        content_ratings (list[CountedOption] | Unset):
        match_scores (list[CountedOption] | Unset):
        published_years (list[CountedOption] | Unset):
        file_sizes (list[CountedOption] | Unset):
        personal_ratings (list[CountedOption] | Unset):
        amazon_ratings (list[CountedOption] | Unset):
        goodreads_ratings (list[CountedOption] | Unset):
        hardcover_ratings (list[CountedOption] | Unset):
        lubimyczytac_ratings (list[CountedOption] | Unset):
        ranobedb_ratings (list[CountedOption] | Unset):
        audible_ratings (list[CountedOption] | Unset):
        page_counts (list[CountedOption] | Unset):
        shelf_statuses (list[CountedOption] | Unset):
        comic_characters (list[CountedOption] | Unset):
        comic_teams (list[CountedOption] | Unset):
        comic_locations (list[CountedOption] | Unset):
        comic_creators (list[CountedOption] | Unset):
        shelves (list[CountedOption] | Unset):
        libraries (list[CountedOption] | Unset):
    """

    authors: list[CountedOption] | Unset = UNSET
    languages: list[LanguageOption] | Unset = UNSET
    read_statuses: list[CountedOption] | Unset = UNSET
    file_types: list[CountedOption] | Unset = UNSET
    categories: list[CountedOption] | Unset = UNSET
    publishers: list[CountedOption] | Unset = UNSET
    series: list[CountedOption] | Unset = UNSET
    tags: list[CountedOption] | Unset = UNSET
    moods: list[CountedOption] | Unset = UNSET
    narrators: list[CountedOption] | Unset = UNSET
    age_ratings: list[CountedOption] | Unset = UNSET
    content_ratings: list[CountedOption] | Unset = UNSET
    match_scores: list[CountedOption] | Unset = UNSET
    published_years: list[CountedOption] | Unset = UNSET
    file_sizes: list[CountedOption] | Unset = UNSET
    personal_ratings: list[CountedOption] | Unset = UNSET
    amazon_ratings: list[CountedOption] | Unset = UNSET
    goodreads_ratings: list[CountedOption] | Unset = UNSET
    hardcover_ratings: list[CountedOption] | Unset = UNSET
    lubimyczytac_ratings: list[CountedOption] | Unset = UNSET
    ranobedb_ratings: list[CountedOption] | Unset = UNSET
    audible_ratings: list[CountedOption] | Unset = UNSET
    page_counts: list[CountedOption] | Unset = UNSET
    shelf_statuses: list[CountedOption] | Unset = UNSET
    comic_characters: list[CountedOption] | Unset = UNSET
    comic_teams: list[CountedOption] | Unset = UNSET
    comic_locations: list[CountedOption] | Unset = UNSET
    comic_creators: list[CountedOption] | Unset = UNSET
    shelves: list[CountedOption] | Unset = UNSET
    libraries: list[CountedOption] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        authors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.authors, Unset):
            authors = []
            for authors_item_data in self.authors:
                authors_item = authors_item_data.to_dict()
                authors.append(authors_item)

        languages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.languages, Unset):
            languages = []
            for languages_item_data in self.languages:
                languages_item = languages_item_data.to_dict()
                languages.append(languages_item)

        read_statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.read_statuses, Unset):
            read_statuses = []
            for read_statuses_item_data in self.read_statuses:
                read_statuses_item = read_statuses_item_data.to_dict()
                read_statuses.append(read_statuses_item)

        file_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.file_types, Unset):
            file_types = []
            for file_types_item_data in self.file_types:
                file_types_item = file_types_item_data.to_dict()
                file_types.append(file_types_item)

        categories: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.categories, Unset):
            categories = []
            for categories_item_data in self.categories:
                categories_item = categories_item_data.to_dict()
                categories.append(categories_item)

        publishers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publishers, Unset):
            publishers = []
            for publishers_item_data in self.publishers:
                publishers_item = publishers_item_data.to_dict()
                publishers.append(publishers_item)

        series: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.series, Unset):
            series = []
            for series_item_data in self.series:
                series_item = series_item_data.to_dict()
                series.append(series_item)

        tags: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = []
            for tags_item_data in self.tags:
                tags_item = tags_item_data.to_dict()
                tags.append(tags_item)

        moods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.moods, Unset):
            moods = []
            for moods_item_data in self.moods:
                moods_item = moods_item_data.to_dict()
                moods.append(moods_item)

        narrators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.narrators, Unset):
            narrators = []
            for narrators_item_data in self.narrators:
                narrators_item = narrators_item_data.to_dict()
                narrators.append(narrators_item)

        age_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.age_ratings, Unset):
            age_ratings = []
            for age_ratings_item_data in self.age_ratings:
                age_ratings_item = age_ratings_item_data.to_dict()
                age_ratings.append(age_ratings_item)

        content_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.content_ratings, Unset):
            content_ratings = []
            for content_ratings_item_data in self.content_ratings:
                content_ratings_item = content_ratings_item_data.to_dict()
                content_ratings.append(content_ratings_item)

        match_scores: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.match_scores, Unset):
            match_scores = []
            for match_scores_item_data in self.match_scores:
                match_scores_item = match_scores_item_data.to_dict()
                match_scores.append(match_scores_item)

        published_years: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.published_years, Unset):
            published_years = []
            for published_years_item_data in self.published_years:
                published_years_item = published_years_item_data.to_dict()
                published_years.append(published_years_item)

        file_sizes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.file_sizes, Unset):
            file_sizes = []
            for file_sizes_item_data in self.file_sizes:
                file_sizes_item = file_sizes_item_data.to_dict()
                file_sizes.append(file_sizes_item)

        personal_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.personal_ratings, Unset):
            personal_ratings = []
            for personal_ratings_item_data in self.personal_ratings:
                personal_ratings_item = personal_ratings_item_data.to_dict()
                personal_ratings.append(personal_ratings_item)

        amazon_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.amazon_ratings, Unset):
            amazon_ratings = []
            for amazon_ratings_item_data in self.amazon_ratings:
                amazon_ratings_item = amazon_ratings_item_data.to_dict()
                amazon_ratings.append(amazon_ratings_item)

        goodreads_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.goodreads_ratings, Unset):
            goodreads_ratings = []
            for goodreads_ratings_item_data in self.goodreads_ratings:
                goodreads_ratings_item = goodreads_ratings_item_data.to_dict()
                goodreads_ratings.append(goodreads_ratings_item)

        hardcover_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hardcover_ratings, Unset):
            hardcover_ratings = []
            for hardcover_ratings_item_data in self.hardcover_ratings:
                hardcover_ratings_item = hardcover_ratings_item_data.to_dict()
                hardcover_ratings.append(hardcover_ratings_item)

        lubimyczytac_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lubimyczytac_ratings, Unset):
            lubimyczytac_ratings = []
            for lubimyczytac_ratings_item_data in self.lubimyczytac_ratings:
                lubimyczytac_ratings_item = lubimyczytac_ratings_item_data.to_dict()
                lubimyczytac_ratings.append(lubimyczytac_ratings_item)

        ranobedb_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ranobedb_ratings, Unset):
            ranobedb_ratings = []
            for ranobedb_ratings_item_data in self.ranobedb_ratings:
                ranobedb_ratings_item = ranobedb_ratings_item_data.to_dict()
                ranobedb_ratings.append(ranobedb_ratings_item)

        audible_ratings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.audible_ratings, Unset):
            audible_ratings = []
            for audible_ratings_item_data in self.audible_ratings:
                audible_ratings_item = audible_ratings_item_data.to_dict()
                audible_ratings.append(audible_ratings_item)

        page_counts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.page_counts, Unset):
            page_counts = []
            for page_counts_item_data in self.page_counts:
                page_counts_item = page_counts_item_data.to_dict()
                page_counts.append(page_counts_item)

        shelf_statuses: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shelf_statuses, Unset):
            shelf_statuses = []
            for shelf_statuses_item_data in self.shelf_statuses:
                shelf_statuses_item = shelf_statuses_item_data.to_dict()
                shelf_statuses.append(shelf_statuses_item)

        comic_characters: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comic_characters, Unset):
            comic_characters = []
            for comic_characters_item_data in self.comic_characters:
                comic_characters_item = comic_characters_item_data.to_dict()
                comic_characters.append(comic_characters_item)

        comic_teams: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comic_teams, Unset):
            comic_teams = []
            for comic_teams_item_data in self.comic_teams:
                comic_teams_item = comic_teams_item_data.to_dict()
                comic_teams.append(comic_teams_item)

        comic_locations: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comic_locations, Unset):
            comic_locations = []
            for comic_locations_item_data in self.comic_locations:
                comic_locations_item = comic_locations_item_data.to_dict()
                comic_locations.append(comic_locations_item)

        comic_creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.comic_creators, Unset):
            comic_creators = []
            for comic_creators_item_data in self.comic_creators:
                comic_creators_item = comic_creators_item_data.to_dict()
                comic_creators.append(comic_creators_item)

        shelves: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shelves, Unset):
            shelves = []
            for shelves_item_data in self.shelves:
                shelves_item = shelves_item_data.to_dict()
                shelves.append(shelves_item)

        libraries: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.libraries, Unset):
            libraries = []
            for libraries_item_data in self.libraries:
                libraries_item = libraries_item_data.to_dict()
                libraries.append(libraries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if authors is not UNSET:
            field_dict["authors"] = authors
        if languages is not UNSET:
            field_dict["languages"] = languages
        if read_statuses is not UNSET:
            field_dict["readStatuses"] = read_statuses
        if file_types is not UNSET:
            field_dict["fileTypes"] = file_types
        if categories is not UNSET:
            field_dict["categories"] = categories
        if publishers is not UNSET:
            field_dict["publishers"] = publishers
        if series is not UNSET:
            field_dict["series"] = series
        if tags is not UNSET:
            field_dict["tags"] = tags
        if moods is not UNSET:
            field_dict["moods"] = moods
        if narrators is not UNSET:
            field_dict["narrators"] = narrators
        if age_ratings is not UNSET:
            field_dict["ageRatings"] = age_ratings
        if content_ratings is not UNSET:
            field_dict["contentRatings"] = content_ratings
        if match_scores is not UNSET:
            field_dict["matchScores"] = match_scores
        if published_years is not UNSET:
            field_dict["publishedYears"] = published_years
        if file_sizes is not UNSET:
            field_dict["fileSizes"] = file_sizes
        if personal_ratings is not UNSET:
            field_dict["personalRatings"] = personal_ratings
        if amazon_ratings is not UNSET:
            field_dict["amazonRatings"] = amazon_ratings
        if goodreads_ratings is not UNSET:
            field_dict["goodreadsRatings"] = goodreads_ratings
        if hardcover_ratings is not UNSET:
            field_dict["hardcoverRatings"] = hardcover_ratings
        if lubimyczytac_ratings is not UNSET:
            field_dict["lubimyczytacRatings"] = lubimyczytac_ratings
        if ranobedb_ratings is not UNSET:
            field_dict["ranobedbRatings"] = ranobedb_ratings
        if audible_ratings is not UNSET:
            field_dict["audibleRatings"] = audible_ratings
        if page_counts is not UNSET:
            field_dict["pageCounts"] = page_counts
        if shelf_statuses is not UNSET:
            field_dict["shelfStatuses"] = shelf_statuses
        if comic_characters is not UNSET:
            field_dict["comicCharacters"] = comic_characters
        if comic_teams is not UNSET:
            field_dict["comicTeams"] = comic_teams
        if comic_locations is not UNSET:
            field_dict["comicLocations"] = comic_locations
        if comic_creators is not UNSET:
            field_dict["comicCreators"] = comic_creators
        if shelves is not UNSET:
            field_dict["shelves"] = shelves
        if libraries is not UNSET:
            field_dict["libraries"] = libraries

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.counted_option import CountedOption
        from ..models.language_option import LanguageOption

        d = dict(src_dict)
        _authors = d.pop("authors", UNSET)
        authors: list[CountedOption] | Unset = UNSET
        if _authors is not UNSET:
            authors = []
            for authors_item_data in _authors:
                authors_item = CountedOption.from_dict(authors_item_data)

                authors.append(authors_item)

        _languages = d.pop("languages", UNSET)
        languages: list[LanguageOption] | Unset = UNSET
        if _languages is not UNSET:
            languages = []
            for languages_item_data in _languages:
                languages_item = LanguageOption.from_dict(languages_item_data)

                languages.append(languages_item)

        _read_statuses = d.pop("readStatuses", UNSET)
        read_statuses: list[CountedOption] | Unset = UNSET
        if _read_statuses is not UNSET:
            read_statuses = []
            for read_statuses_item_data in _read_statuses:
                read_statuses_item = CountedOption.from_dict(read_statuses_item_data)

                read_statuses.append(read_statuses_item)

        _file_types = d.pop("fileTypes", UNSET)
        file_types: list[CountedOption] | Unset = UNSET
        if _file_types is not UNSET:
            file_types = []
            for file_types_item_data in _file_types:
                file_types_item = CountedOption.from_dict(file_types_item_data)

                file_types.append(file_types_item)

        _categories = d.pop("categories", UNSET)
        categories: list[CountedOption] | Unset = UNSET
        if _categories is not UNSET:
            categories = []
            for categories_item_data in _categories:
                categories_item = CountedOption.from_dict(categories_item_data)

                categories.append(categories_item)

        _publishers = d.pop("publishers", UNSET)
        publishers: list[CountedOption] | Unset = UNSET
        if _publishers is not UNSET:
            publishers = []
            for publishers_item_data in _publishers:
                publishers_item = CountedOption.from_dict(publishers_item_data)

                publishers.append(publishers_item)

        _series = d.pop("series", UNSET)
        series: list[CountedOption] | Unset = UNSET
        if _series is not UNSET:
            series = []
            for series_item_data in _series:
                series_item = CountedOption.from_dict(series_item_data)

                series.append(series_item)

        _tags = d.pop("tags", UNSET)
        tags: list[CountedOption] | Unset = UNSET
        if _tags is not UNSET:
            tags = []
            for tags_item_data in _tags:
                tags_item = CountedOption.from_dict(tags_item_data)

                tags.append(tags_item)

        _moods = d.pop("moods", UNSET)
        moods: list[CountedOption] | Unset = UNSET
        if _moods is not UNSET:
            moods = []
            for moods_item_data in _moods:
                moods_item = CountedOption.from_dict(moods_item_data)

                moods.append(moods_item)

        _narrators = d.pop("narrators", UNSET)
        narrators: list[CountedOption] | Unset = UNSET
        if _narrators is not UNSET:
            narrators = []
            for narrators_item_data in _narrators:
                narrators_item = CountedOption.from_dict(narrators_item_data)

                narrators.append(narrators_item)

        _age_ratings = d.pop("ageRatings", UNSET)
        age_ratings: list[CountedOption] | Unset = UNSET
        if _age_ratings is not UNSET:
            age_ratings = []
            for age_ratings_item_data in _age_ratings:
                age_ratings_item = CountedOption.from_dict(age_ratings_item_data)

                age_ratings.append(age_ratings_item)

        _content_ratings = d.pop("contentRatings", UNSET)
        content_ratings: list[CountedOption] | Unset = UNSET
        if _content_ratings is not UNSET:
            content_ratings = []
            for content_ratings_item_data in _content_ratings:
                content_ratings_item = CountedOption.from_dict(content_ratings_item_data)

                content_ratings.append(content_ratings_item)

        _match_scores = d.pop("matchScores", UNSET)
        match_scores: list[CountedOption] | Unset = UNSET
        if _match_scores is not UNSET:
            match_scores = []
            for match_scores_item_data in _match_scores:
                match_scores_item = CountedOption.from_dict(match_scores_item_data)

                match_scores.append(match_scores_item)

        _published_years = d.pop("publishedYears", UNSET)
        published_years: list[CountedOption] | Unset = UNSET
        if _published_years is not UNSET:
            published_years = []
            for published_years_item_data in _published_years:
                published_years_item = CountedOption.from_dict(published_years_item_data)

                published_years.append(published_years_item)

        _file_sizes = d.pop("fileSizes", UNSET)
        file_sizes: list[CountedOption] | Unset = UNSET
        if _file_sizes is not UNSET:
            file_sizes = []
            for file_sizes_item_data in _file_sizes:
                file_sizes_item = CountedOption.from_dict(file_sizes_item_data)

                file_sizes.append(file_sizes_item)

        _personal_ratings = d.pop("personalRatings", UNSET)
        personal_ratings: list[CountedOption] | Unset = UNSET
        if _personal_ratings is not UNSET:
            personal_ratings = []
            for personal_ratings_item_data in _personal_ratings:
                personal_ratings_item = CountedOption.from_dict(personal_ratings_item_data)

                personal_ratings.append(personal_ratings_item)

        _amazon_ratings = d.pop("amazonRatings", UNSET)
        amazon_ratings: list[CountedOption] | Unset = UNSET
        if _amazon_ratings is not UNSET:
            amazon_ratings = []
            for amazon_ratings_item_data in _amazon_ratings:
                amazon_ratings_item = CountedOption.from_dict(amazon_ratings_item_data)

                amazon_ratings.append(amazon_ratings_item)

        _goodreads_ratings = d.pop("goodreadsRatings", UNSET)
        goodreads_ratings: list[CountedOption] | Unset = UNSET
        if _goodreads_ratings is not UNSET:
            goodreads_ratings = []
            for goodreads_ratings_item_data in _goodreads_ratings:
                goodreads_ratings_item = CountedOption.from_dict(goodreads_ratings_item_data)

                goodreads_ratings.append(goodreads_ratings_item)

        _hardcover_ratings = d.pop("hardcoverRatings", UNSET)
        hardcover_ratings: list[CountedOption] | Unset = UNSET
        if _hardcover_ratings is not UNSET:
            hardcover_ratings = []
            for hardcover_ratings_item_data in _hardcover_ratings:
                hardcover_ratings_item = CountedOption.from_dict(hardcover_ratings_item_data)

                hardcover_ratings.append(hardcover_ratings_item)

        _lubimyczytac_ratings = d.pop("lubimyczytacRatings", UNSET)
        lubimyczytac_ratings: list[CountedOption] | Unset = UNSET
        if _lubimyczytac_ratings is not UNSET:
            lubimyczytac_ratings = []
            for lubimyczytac_ratings_item_data in _lubimyczytac_ratings:
                lubimyczytac_ratings_item = CountedOption.from_dict(lubimyczytac_ratings_item_data)

                lubimyczytac_ratings.append(lubimyczytac_ratings_item)

        _ranobedb_ratings = d.pop("ranobedbRatings", UNSET)
        ranobedb_ratings: list[CountedOption] | Unset = UNSET
        if _ranobedb_ratings is not UNSET:
            ranobedb_ratings = []
            for ranobedb_ratings_item_data in _ranobedb_ratings:
                ranobedb_ratings_item = CountedOption.from_dict(ranobedb_ratings_item_data)

                ranobedb_ratings.append(ranobedb_ratings_item)

        _audible_ratings = d.pop("audibleRatings", UNSET)
        audible_ratings: list[CountedOption] | Unset = UNSET
        if _audible_ratings is not UNSET:
            audible_ratings = []
            for audible_ratings_item_data in _audible_ratings:
                audible_ratings_item = CountedOption.from_dict(audible_ratings_item_data)

                audible_ratings.append(audible_ratings_item)

        _page_counts = d.pop("pageCounts", UNSET)
        page_counts: list[CountedOption] | Unset = UNSET
        if _page_counts is not UNSET:
            page_counts = []
            for page_counts_item_data in _page_counts:
                page_counts_item = CountedOption.from_dict(page_counts_item_data)

                page_counts.append(page_counts_item)

        _shelf_statuses = d.pop("shelfStatuses", UNSET)
        shelf_statuses: list[CountedOption] | Unset = UNSET
        if _shelf_statuses is not UNSET:
            shelf_statuses = []
            for shelf_statuses_item_data in _shelf_statuses:
                shelf_statuses_item = CountedOption.from_dict(shelf_statuses_item_data)

                shelf_statuses.append(shelf_statuses_item)

        _comic_characters = d.pop("comicCharacters", UNSET)
        comic_characters: list[CountedOption] | Unset = UNSET
        if _comic_characters is not UNSET:
            comic_characters = []
            for comic_characters_item_data in _comic_characters:
                comic_characters_item = CountedOption.from_dict(comic_characters_item_data)

                comic_characters.append(comic_characters_item)

        _comic_teams = d.pop("comicTeams", UNSET)
        comic_teams: list[CountedOption] | Unset = UNSET
        if _comic_teams is not UNSET:
            comic_teams = []
            for comic_teams_item_data in _comic_teams:
                comic_teams_item = CountedOption.from_dict(comic_teams_item_data)

                comic_teams.append(comic_teams_item)

        _comic_locations = d.pop("comicLocations", UNSET)
        comic_locations: list[CountedOption] | Unset = UNSET
        if _comic_locations is not UNSET:
            comic_locations = []
            for comic_locations_item_data in _comic_locations:
                comic_locations_item = CountedOption.from_dict(comic_locations_item_data)

                comic_locations.append(comic_locations_item)

        _comic_creators = d.pop("comicCreators", UNSET)
        comic_creators: list[CountedOption] | Unset = UNSET
        if _comic_creators is not UNSET:
            comic_creators = []
            for comic_creators_item_data in _comic_creators:
                comic_creators_item = CountedOption.from_dict(comic_creators_item_data)

                comic_creators.append(comic_creators_item)

        _shelves = d.pop("shelves", UNSET)
        shelves: list[CountedOption] | Unset = UNSET
        if _shelves is not UNSET:
            shelves = []
            for shelves_item_data in _shelves:
                shelves_item = CountedOption.from_dict(shelves_item_data)

                shelves.append(shelves_item)

        _libraries = d.pop("libraries", UNSET)
        libraries: list[CountedOption] | Unset = UNSET
        if _libraries is not UNSET:
            libraries = []
            for libraries_item_data in _libraries:
                libraries_item = CountedOption.from_dict(libraries_item_data)

                libraries.append(libraries_item)

        app_filter_options = cls(
            authors=authors,
            languages=languages,
            read_statuses=read_statuses,
            file_types=file_types,
            categories=categories,
            publishers=publishers,
            series=series,
            tags=tags,
            moods=moods,
            narrators=narrators,
            age_ratings=age_ratings,
            content_ratings=content_ratings,
            match_scores=match_scores,
            published_years=published_years,
            file_sizes=file_sizes,
            personal_ratings=personal_ratings,
            amazon_ratings=amazon_ratings,
            goodreads_ratings=goodreads_ratings,
            hardcover_ratings=hardcover_ratings,
            lubimyczytac_ratings=lubimyczytac_ratings,
            ranobedb_ratings=ranobedb_ratings,
            audible_ratings=audible_ratings,
            page_counts=page_counts,
            shelf_statuses=shelf_statuses,
            comic_characters=comic_characters,
            comic_teams=comic_teams,
            comic_locations=comic_locations,
            comic_creators=comic_creators,
            shelves=shelves,
            libraries=libraries,
        )

        app_filter_options.additional_properties = d
        return app_filter_options

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
