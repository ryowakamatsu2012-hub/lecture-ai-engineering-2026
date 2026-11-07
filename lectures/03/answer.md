# 第3回 解答

## 実施したこと

- `app/tools.py` に `make_quiz(lecture: int) -> str` を追加した。用語集から指定した回の用語をランダムに1つ選び、「用語の意味は？」という問題と定義をJSON形式で返す。該当する用語がない場合は、その旨を返す。
- `app/agent.py` に `make_quiz` を登録し、モデルから利用できるようにした。
- `INSTRUCTIONS` に、回答の後に関連記事を探して載せる指示を追加した。

## 実行結果

- `uv run python -m app.agent --list-tools` で `search_glossary`、`get_lecture_summary`、`make_quiz` の3つが表示された。
- `uv run python -m app.agent --trace "第2回の内容から確認問題を1問出して"` を実行すると、`make_quiz({'lecture': 2})` が呼び出された。今回は「エポック」の意味を尋ねる問題が出力された。
- トレース上の利用状況は `requests=2`、`tool_calls=1` だった。
- `uv run pytest -q` は16件すべて成功した。
