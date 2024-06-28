# LidemyOJ

## Getting Started

```
python 1036.py < input.in
```

Comparison correct

```
python 1036.py < input.in > temp_output.in

diff temp_output.in result.in
```

## Question(TW)

[LidemyOJ](https://oj.lidemy.com/)

## Additional

javascript

```
cat input.in | node 1036.js | diff result.in -
```

When you are developing or collaborating across different platforms, you don't need to worry about the differences in line endings between systems; you only need to focus on the actual content of the text. The `--strip-trailing-cr` option removes the carriage return characters from the output, so that the diff command can focus on the actual content of the text.

```
cat input.in | node 1036.js | diff --strip-trailing-cr result.in -
```
