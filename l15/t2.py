import logging

logging.basicConfig(
    filename='t2.log',
    encoding='utf-8',
    format='{asctime} {levelname} {funcName}->{lineno}: {msg}',
    style='{',
    level=logging.NOTSET
)

logger = logging.getLogger(__name__)




class NewYearThree():
    DEFAULT_HEIGHT = 5
    DEFAULT_SYMBOL = '#'

    def __init__(self, height, symbol):
        self.height = height
        self.symbol = symbol


    def draw(self):
        """
        >>> NewYearThree(3, '@').draw()
        '   @\\n  @@@\\n @@@@@'
        >>> NewYearThree(-1, '*').draw()
        '     *\\n    ***\\n   *****\\n  *******\\n *********'
        >>> NewYearThree(0, ' ').draw()
        '     #\\n    ###\\n   #####\\n  #######\\n #########'
        """
        if self.height == 0:
            logger.warning('Ввели 0 (ноль), таких елок нет(')
            self.height = self.DEFAULT_HEIGHT
        elif self.height < 0:
            logger.warning('Ввели отрицательную высоту, таких елок нет(')
            self.height = self.DEFAULT_HEIGHT

        if not self.symbol.strip():
            logger.warning('Ввели пустой символ, таких елок нет(')
            self.symbol = self.DEFAULT_SYMBOL

        logger.info(f'Ща выдам елку высотой {self.height} из {self.symbol}')
        tree = []

        for x in range(self.height):
            margin = ' ' * (self.height - x)
            side = x * self.symbol
            tree.append(margin + side + self.symbol + side)
        return '\n'.join(tree)




if __name__ == '__main__':
    import doctest
    doctest.testmod()


# Trying:
#     NewYearThree(3, '@').draw()
# Expecting:
#     '   @\n  @@@\n @@@@@'
# ok
# Trying:
#     NewYearThree(-1, '*').draw()
# Expecting:
#     '     *\n    ***\n   *****\n  *******\n *********'
# ok
# Trying:
#     NewYearThree(0, ' ').draw()
# Expecting:
#     '     #\n    ###\n   #####\n  #######\n #########'
# ok
# 3 items had no tests:
#     t2
#     t2.NewYearThree
#     t2.NewYearThree.__init__
# 1 items passed all tests:
#    3 tests in t2.NewYearThree.draw
# 3 tests in 4 items.
# 3 passed and 0 failed.
# Test passed.