# 第3回 解答

## 実施したこと

- `app/tools.py` に `make_quiz(lecture: int) -> str` を追加した。用語集から指定した回の用語をランダムに1つ選び、「用語の意味は？」という問題と定義をJSON形式で返す。該当する用語がない場合は、その旨を返す。
- `app/agent.py` に `make_quiz` を登録し、モデルから利用できるようにした。
- `INSTRUCTIONS` に、回答の後に関連記事を探して載せる指示を追加した。

## 宿題（基礎）

`search_glossary` の docstring を変更し、「用語や講座に固有のことを答える前に使う」方針は保ったまま、複数用語を比較するときは検索語をまとめて渡すようにした（例: `LoRAとQLoRA`）。

同じ質問 `LoRAとQLoRAの違いは？` を `--trace` 付きで変更前後に実行した。

- 変更前: `search_glossary` が `LoRA` と `QLoRA` で別々に呼ばれ、`tool_calls=2`。回答では各用語の定義を個別に説明した。
- 変更後: `search_glossary` が `LoRAとQLoRA` で1回呼ばれ、用語集から両方の定義が返り、`tool_calls=1`。回答では両者の違いを先に示してから、それぞれの特徴を説明した。
- 両方とも LLM 呼び出し回数は `requests=2`。用語集を確認する動作と回答内容の要点は保たれたまま、検索回数が1回減った。

## 実行結果

- `uv run python -m app.agent --list-tools` で `search_glossary`、`get_lecture_summary`、`make_quiz` の3つが表示された。
- `uv run python -m app.agent --trace "第2回の内容から確認問題を1問出して"` を実行すると、`make_quiz({'lecture': 2})` が呼び出された。今回は「エポック」の意味を尋ねる問題が出力された。
- トレース上の利用状況は `requests=2`、`tool_calls=1` だった。
- `uv run pytest -q` は16件すべて成功した。
