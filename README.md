# Tikkurila Paint Searcher
Script that allows to find the closest color in *Tikkurila Symphony 2436* palette

After input RGB data of color program returns 5 most close colors in palette with links and indexes of them

# Performance test of scraping
It's a lot of links and data to scrap, so I have that idea that I can use multithreading to scrap links in parallel way.
I just kinda say wow, when I saw the results, after added ThreadPool with 30 processes execution, time is **95%** faster than the old one.
So instead of waiting something like 30 minutes, scraping finished in 2 minutes. That's awesome.

