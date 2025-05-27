# Yomitan API

## API Paths

### `serverVersion`

Returns the version of the native messaging component.

#### Request

- Request method: `POST`

#### Response Example (200)

```json
{
    "version": 1
}
```

### `yomitanVersion`

Returns Yomitan's version.

#### Request

- Request method: `POST`

#### Response Example (200)

```json
{
    "version": "0.0.0.0"
}
```

### `termEntries`

Returns term dictionary entries for search text as they are represented internally by Yomitan.

#### Request

- Request method: `POST`

- Body: 
    ```json
    {

    }
    ```

#### Response Example (200)

```json

```

### `kanjiEntries`

Returns kanji dictionary entries for search text as they are represented internally by Yomitan.

#### Request

- Request method: `POST`

- Body: 
    ```json
    {

    }
    ```

#### Response Example (200)

```json

```

### `/ankiFields`

Returns rendered Anki handlebars for a 

#### Request

- Request method: `POST`

- Body: 
    ```json
    {

    }
    ```

#### Response Example (200)

```json

```
