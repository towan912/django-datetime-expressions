# django-datetime-expressions

`django-datetime-expressions`は、Django ORMで日時操作を簡単に行うためのカスタム式を提供します。
日時フィールドに対して相対的な加算や減算が可能です。

**[English Version](README.md)**

## 特徴

- 日時フィールドに対する相対的な操作（例: 日、週、月、年の加算/減算）
- 複数のデータベースエンジン（MySQL, SQLite, Oracle）に対応
- `EXTRACT`を使用したエポックタイムの取得

## インストール

```bash
pip install django-datetime-expressions
```

## 使用方法

以下は、`RelativeDay`を使用して日付を操作する例です。

```python
from datetime import datetime
from django.db.models import F
from datetime_expressions import RelativeDay

# 例: 現在の日付に5日を加算
queryset = MyModel.objects.annotate(new_date=RelativeDay(F('date_field'), 5))
```

### サポートされる相対操作

| クラス名          | 説明               | 単位       |
|-------------------|--------------------|------------|
| `RelativeDay`     | 日の加算/減算      | 日         |
| `RelativeWeek`    | 週の加算/減算      | 7日単位    |
| `RelativeMonth`   | 月の加算/減算      | 月         |
| `RelativeYear`    | 年の加算/減算      | 年         |
| `RelativeHour`    | 時間の加算/減算    | 時間       |
| `RelativeMinute`  | 分の加算/減算      | 分         |
| `RelativeSecond`  | 秒の加算/減算      | 秒         |

### エポックタイムの取得

`Epoch`クラスを使用して、日時フィールドからエポックタイム（1970年1月1日からの秒数）を取得できます。

```python
from datetime_expressions import Epoch

queryset = MyModel.objects.annotate(epoch_time=Epoch(F('date_field')))
```

## サポートされるデータベース

- MySQL
- SQLite
- Oracle

## 貢献

バグ報告や機能リクエストは、[GitHub Issues](https://github.com/towan912/django-datetime-expressions/issues)で受け付けています。

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。詳細は[LICENSE](LICENSE)ファイルをご覧ください。