Note why the models.base and models.ceo refactor works:

In all honesty, I had to ask chatGPT why we were doing this and I learned a lot when I did.

The main benefit was to keep files organized and imporve maintainability. Each file has a focused responsability.

I did not know that by creating the **init** .py file that python recognizes it as a package.
