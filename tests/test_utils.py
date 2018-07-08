import os

from conftest import TEST_DATA_DIR


def test_add_offset():
    from hnccorr.utils import add_offset_coordinates

    assert add_offset_coordinates((1, 2), (3, 4)) == (4, 6)


def test_add_set_offset():
    from hnccorr.utils import add_offset_set_coordinates

    assert add_offset_set_coordinates({(0, 1), (1, 1)}, (2, 2)) == {
        (2, 3),
        (3, 3),
    }


def test_add_time_index():
    from hnccorr.utils import add_time_index

    assert add_time_index((5, 4)) == (slice(None, None), 5, 4)


def test_list_images():
    from hnccorr.utils import list_images

    images = list_images(TEST_DATA_DIR)
    expected_images = map(
        lambda x: os.path.join("./test_data/simple_movie", x),
        [
            "simple_movie00000.tif",
            "simple_movie00001.tif",
            "simple_movie00002.tif",
        ],
    )

    for i, e in zip(images, expected_images):
        assert os.path.abspath(i) == os.path.abspath(e)


def test_fill_holes():
    from hnccorr.utils import fill_holes

    assert fill_holes({(1,), (3,)}, (5,)) == {(1,), (2,), (3,)}


def test_select_max_seed_component():
    from hnccorr.utils import select_max_seed_component

    assert select_max_seed_component(
        {(1,), (2,), (5,), (6,)}, {(1,), (2,), (5,)}, 1
    ) == {(1,), (2,)}


def test_eight_neighborhood():
    from hnccorr.utils import eight_neighborhood

    assert eight_neighborhood(1, 1) == {(-1,), (0,), (1,)}
    assert eight_neighborhood(1, 2) == {(-2,), (-1,), (0,), (1,), (2,)}
    assert eight_neighborhood(2, 1) == {
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    }


def test_generate_pixles():
    from hnccorr.utils import generate_pixels

    assert set(generate_pixels((1, 2))) == {(0, 0), (0, 1)}
