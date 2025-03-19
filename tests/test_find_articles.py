def test_is_there_more_than_1_cloud_dev_ops_article(articles_cached):
    cloud_and_dev_ops_articles = articles_cached[0]
    assert len(cloud_and_dev_ops_articles) > 1


def test_is_there_more_than_1_top_article(articles_cached):
    top_articles = articles_cached[1]
    assert len(top_articles) > 1


def test_are_articles_different(articles_cached):
    cloud_and_dev_ops_articles = articles_cached[0]
    top_articles = articles_cached[1]
    assert cloud_and_dev_ops_articles is not top_articles
