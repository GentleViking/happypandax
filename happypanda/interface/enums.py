from happypanda.common import utils


class ViewType(utils.APIEnum):
    #: Library
    Library = 0
    #: Favourite
    Favorite = 1
    #: Inbox
    Inbox = 2


class ItemType(utils.APIEnum):
    #: Gallery
    Gallery = 0
    #: Collection
    Collection = 1
    #: GalleryFilter
    GalleryFilter = 2
    #: Page
    Page = 3
    #: Grouping
    Grouping = 4


class ImageSize(utils.APIEnum):
    #: Original
    Original = utils.ImageSize(0, 0)
    #: Big
    Big = utils.ImageSize(200, 400)
    #: Medium
    Medium = utils.ImageSize(100, 250)
    #: Small
    Small = utils.ImageSize(50, 100)