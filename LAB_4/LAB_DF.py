{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 29,
      "metadata": {
        "id": "PrBHJNPL85F8"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.ensemble import RandomForestClassifier\n",
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df = pd.read_csv('logs.csv')"
      ],
      "metadata": {
        "id": "WM5XLwMA-Z9o"
      },
      "execution_count": 30,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 478
        },
        "id": "uXM3QIy0-jVn",
        "outputId": "b3cea3ec-e8f5-4ed8-8fda-62db2eff2ea9"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "       Source Port  Destination Port  NAT Source Port  NAT Destination Port  \\\n",
              "0            57222                53            54587                    53   \n",
              "1            56258              3389            56258                  3389   \n",
              "2             6881             50321            43265                 50321   \n",
              "3            50553              3389            50553                  3389   \n",
              "4            50002               443            45848                   443   \n",
              "...            ...               ...              ...                   ...   \n",
              "65527        63691                80            13237                    80   \n",
              "65528        50964                80            13485                    80   \n",
              "65529        54871               445                0                     0   \n",
              "65530        54870               445                0                     0   \n",
              "65531        54867               445                0                     0   \n",
              "\n",
              "       Action    Bytes  Bytes Sent  Bytes Received  Packets  \\\n",
              "0           0      177          94              83        2   \n",
              "1           0     4768        1600            3168       19   \n",
              "2           0      238         118             120        2   \n",
              "3           0     3327        1438            1889       15   \n",
              "4           0    25358        6778           18580       31   \n",
              "...       ...      ...         ...             ...      ...   \n",
              "65527       0      314         192             122        6   \n",
              "65528       0  4680740       67312         4613428     4675   \n",
              "65529       2       70          70               0        1   \n",
              "65530       2       70          70               0        1   \n",
              "65531       2       70          70               0        1   \n",
              "\n",
              "       Elapsed Time (sec)  pkts_sent  pkts_received  \n",
              "0                      30          1              1  \n",
              "1                      17         10              9  \n",
              "2                    1199          1              1  \n",
              "3                      17          8              7  \n",
              "4                      16         13             18  \n",
              "...                   ...        ...            ...  \n",
              "65527                  15          4              2  \n",
              "65528                  77        985           3690  \n",
              "65529                   0          1              0  \n",
              "65530                   0          1              0  \n",
              "65531                   0          1              0  \n",
              "\n",
              "[65532 rows x 12 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-17a18e98-da0f-4a49-9a3f-e38623d988f1\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Source Port</th>\n",
              "      <th>Destination Port</th>\n",
              "      <th>NAT Source Port</th>\n",
              "      <th>NAT Destination Port</th>\n",
              "      <th>Action</th>\n",
              "      <th>Bytes</th>\n",
              "      <th>Bytes Sent</th>\n",
              "      <th>Bytes Received</th>\n",
              "      <th>Packets</th>\n",
              "      <th>Elapsed Time (sec)</th>\n",
              "      <th>pkts_sent</th>\n",
              "      <th>pkts_received</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>57222</td>\n",
              "      <td>53</td>\n",
              "      <td>54587</td>\n",
              "      <td>53</td>\n",
              "      <td>0</td>\n",
              "      <td>177</td>\n",
              "      <td>94</td>\n",
              "      <td>83</td>\n",
              "      <td>2</td>\n",
              "      <td>30</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>56258</td>\n",
              "      <td>3389</td>\n",
              "      <td>56258</td>\n",
              "      <td>3389</td>\n",
              "      <td>0</td>\n",
              "      <td>4768</td>\n",
              "      <td>1600</td>\n",
              "      <td>3168</td>\n",
              "      <td>19</td>\n",
              "      <td>17</td>\n",
              "      <td>10</td>\n",
              "      <td>9</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>6881</td>\n",
              "      <td>50321</td>\n",
              "      <td>43265</td>\n",
              "      <td>50321</td>\n",
              "      <td>0</td>\n",
              "      <td>238</td>\n",
              "      <td>118</td>\n",
              "      <td>120</td>\n",
              "      <td>2</td>\n",
              "      <td>1199</td>\n",
              "      <td>1</td>\n",
              "      <td>1</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>50553</td>\n",
              "      <td>3389</td>\n",
              "      <td>50553</td>\n",
              "      <td>3389</td>\n",
              "      <td>0</td>\n",
              "      <td>3327</td>\n",
              "      <td>1438</td>\n",
              "      <td>1889</td>\n",
              "      <td>15</td>\n",
              "      <td>17</td>\n",
              "      <td>8</td>\n",
              "      <td>7</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>50002</td>\n",
              "      <td>443</td>\n",
              "      <td>45848</td>\n",
              "      <td>443</td>\n",
              "      <td>0</td>\n",
              "      <td>25358</td>\n",
              "      <td>6778</td>\n",
              "      <td>18580</td>\n",
              "      <td>31</td>\n",
              "      <td>16</td>\n",
              "      <td>13</td>\n",
              "      <td>18</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>65527</th>\n",
              "      <td>63691</td>\n",
              "      <td>80</td>\n",
              "      <td>13237</td>\n",
              "      <td>80</td>\n",
              "      <td>0</td>\n",
              "      <td>314</td>\n",
              "      <td>192</td>\n",
              "      <td>122</td>\n",
              "      <td>6</td>\n",
              "      <td>15</td>\n",
              "      <td>4</td>\n",
              "      <td>2</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>65528</th>\n",
              "      <td>50964</td>\n",
              "      <td>80</td>\n",
              "      <td>13485</td>\n",
              "      <td>80</td>\n",
              "      <td>0</td>\n",
              "      <td>4680740</td>\n",
              "      <td>67312</td>\n",
              "      <td>4613428</td>\n",
              "      <td>4675</td>\n",
              "      <td>77</td>\n",
              "      <td>985</td>\n",
              "      <td>3690</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>65529</th>\n",
              "      <td>54871</td>\n",
              "      <td>445</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>70</td>\n",
              "      <td>70</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>65530</th>\n",
              "      <td>54870</td>\n",
              "      <td>445</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>70</td>\n",
              "      <td>70</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>65531</th>\n",
              "      <td>54867</td>\n",
              "      <td>445</td>\n",
              "      <td>0</td>\n",
              "      <td>0</td>\n",
              "      <td>2</td>\n",
              "      <td>70</td>\n",
              "      <td>70</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "      <td>1</td>\n",
              "      <td>0</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>65532 rows × 12 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-17a18e98-da0f-4a49-9a3f-e38623d988f1')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-17a18e98-da0f-4a49-9a3f-e38623d988f1 button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-17a18e98-da0f-4a49-9a3f-e38623d988f1');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-b521a379-2c8d-4879-942b-acf558e12983\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-b521a379-2c8d-4879-942b-acf558e12983')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-b521a379-2c8d-4879-942b-acf558e12983 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df",
              "summary": "{\n  \"name\": \"df\",\n  \"rows\": 65532,\n  \"fields\": [\n    {\n      \"column\": \"Source Port\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 15255,\n        \"min\": 0,\n        \"max\": 65534,\n        \"num_unique_values\": 22724,\n        \"samples\": [\n          63125,\n          62417,\n          55918\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Destination Port\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 18466,\n        \"min\": 0,\n        \"max\": 65535,\n        \"num_unique_values\": 3273,\n        \"samples\": [\n          37828,\n          51819,\n          28520\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NAT Source Port\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 21970,\n        \"min\": 0,\n        \"max\": 65535,\n        \"num_unique_values\": 29152,\n        \"samples\": [\n          40540,\n          35838,\n          8160\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"NAT Destination Port\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 9739,\n        \"min\": 0,\n        \"max\": 65535,\n        \"num_unique_values\": 2533,\n        \"samples\": [\n          31151,\n          33531,\n          8080\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Action\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 0,\n        \"min\": 0,\n        \"max\": 3,\n        \"num_unique_values\": 4,\n        \"samples\": [\n          2,\n          3,\n          0\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Bytes\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 5618438,\n        \"min\": 60,\n        \"max\": 1269359015,\n        \"num_unique_values\": 10724,\n        \"samples\": [\n          6387,\n          1570,\n          24712\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Bytes Sent\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3828138,\n        \"min\": 60,\n        \"max\": 948477220,\n        \"num_unique_values\": 6683,\n        \"samples\": [\n          77974,\n          9715,\n          5331\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Bytes Received\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2463207,\n        \"min\": 0,\n        \"max\": 320881795,\n        \"num_unique_values\": 8814,\n        \"samples\": [\n          2098,\n          1307,\n          21406\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Packets\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 5133,\n        \"min\": 1,\n        \"max\": 1036116,\n        \"num_unique_values\": 1116,\n        \"samples\": [\n          627,\n          44,\n          21027\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"Elapsed Time (sec)\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 302,\n        \"min\": 0,\n        \"max\": 10824,\n        \"num_unique_values\": 915,\n        \"samples\": [\n          132,\n          757,\n          163\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"pkts_sent\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 3218,\n        \"min\": 1,\n        \"max\": 747520,\n        \"num_unique_values\": 749,\n        \"samples\": [\n          504,\n          39649,\n          91\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    },\n    {\n      \"column\": \"pkts_received\",\n      \"properties\": {\n        \"dtype\": \"number\",\n        \"std\": 2223,\n        \"min\": 0,\n        \"max\": 327208,\n        \"num_unique_values\": 922,\n        \"samples\": [\n          1681,\n          67,\n          699\n        ],\n        \"semantic_type\": \"\",\n        \"description\": \"\"\n      }\n    }\n  ]\n}"
            }
          },
          "metadata": {},
          "execution_count": 31
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df_null = df.isnull().sum()"
      ],
      "metadata": {
        "id": "5IPAtxA_AdGA"
      },
      "execution_count": 34,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_null"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8-iGYSLIBlKb",
        "outputId": "3c22e62d-4e29-44dd-cfb2-1821f7cf66e7"
      },
      "execution_count": 35,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Source Port             0\n",
              "Destination Port        0\n",
              "NAT Source Port         0\n",
              "NAT Destination Port    0\n",
              "Action                  0\n",
              "Bytes                   0\n",
              "Bytes Sent              0\n",
              "Bytes Received          0\n",
              "Packets                 0\n",
              "Elapsed Time (sec)      0\n",
              "pkts_sent               0\n",
              "pkts_received           0\n",
              "dtype: int64"
            ]
          },
          "metadata": {},
          "execution_count": 35
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "X = df.drop(columns=['Action'])\n",
        "y = df['Action']"
      ],
      "metadata": {
        "id": "_crd9fAY-0y2"
      },
      "execution_count": 36,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
      ],
      "metadata": {
        "id": "-DhS18UZ-2pF"
      },
      "execution_count": 38,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = RandomForestClassifier(n_estimators=100, random_state=42)\n",
        "model.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 74
        },
        "id": "0W2HDkM6_t0e",
        "outputId": "9cb459d7-5dd5-43dc-9549-090e05328054"
      },
      "execution_count": 39,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RandomForestClassifier(random_state=42)"
            ],
            "text/html": [
              "<style>#sk-container-id-2 {color: black;background-color: white;}#sk-container-id-2 pre{padding: 0;}#sk-container-id-2 div.sk-toggleable {background-color: white;}#sk-container-id-2 label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-container-id-2 label.sk-toggleable__label-arrow:before {content: \"▸\";float: left;margin-right: 0.25em;color: #696969;}#sk-container-id-2 label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-container-id-2 div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-container-id-2 div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-container-id-2 div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-container-id-2 input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-container-id-2 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: \"▾\";}#sk-container-id-2 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-container-id-2 div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-container-id-2 div.sk-estimator:hover {background-color: #d4ebff;}#sk-container-id-2 div.sk-parallel-item::after {content: \"\";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-container-id-2 div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-container-id-2 div.sk-serial::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: 0;}#sk-container-id-2 div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;position: relative;}#sk-container-id-2 div.sk-item {position: relative;z-index: 1;}#sk-container-id-2 div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;position: relative;}#sk-container-id-2 div.sk-item::before, #sk-container-id-2 div.sk-parallel-item::before {content: \"\";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 0;bottom: 0;left: 50%;z-index: -1;}#sk-container-id-2 div.sk-parallel-item {display: flex;flex-direction: column;z-index: 1;position: relative;background-color: white;}#sk-container-id-2 div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-container-id-2 div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-container-id-2 div.sk-parallel-item:only-child::after {width: 0;}#sk-container-id-2 div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;}#sk-container-id-2 div.sk-label label {font-family: monospace;font-weight: bold;display: inline-block;line-height: 1.2em;}#sk-container-id-2 div.sk-label-container {text-align: center;}#sk-container-id-2 div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-container-id-2 div.sk-text-repr-fallback {display: none;}</style><div id=\"sk-container-id-2\" class=\"sk-top-container\"><div class=\"sk-text-repr-fallback\"><pre>RandomForestClassifier(random_state=42)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class=\"sk-container\" hidden><div class=\"sk-item\"><div class=\"sk-estimator sk-toggleable\"><input class=\"sk-toggleable__control sk-hidden--visually\" id=\"sk-estimator-id-2\" type=\"checkbox\" checked><label for=\"sk-estimator-id-2\" class=\"sk-toggleable__label sk-toggleable__label-arrow\">RandomForestClassifier</label><div class=\"sk-toggleable__content\"><pre>RandomForestClassifier(random_state=42)</pre></div></div></div></div></div>"
            ]
          },
          "metadata": {},
          "execution_count": 39
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "y_pred = model.predict(X_test)"
      ],
      "metadata": {
        "id": "7uc6GJTZ_9Wy"
      },
      "execution_count": 40,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "accuracy = accuracy_score(y_test, y_pred)\n",
        "print(f'Accuracy: {accuracy:.2f}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4Y6xNrpdAAHF",
        "outputId": "4268927d-b5f9-4e70-b5b7-bfe0b33b1f4d"
      },
      "execution_count": 43,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Accuracy: 1.00\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('Classification Report:')\n",
        "print(classification_report(y_test, y_pred, target_names=['allow', 'deny', 'drop', 'reset-both']))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uhOuxhy4AVmG",
        "outputId": "205be3c7-e511-429e-8a9f-25488f16bae8"
      },
      "execution_count": 44,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Classification Report:\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "       allow       1.00      1.00      1.00      7545\n",
            "        deny       1.00      1.00      1.00      2994\n",
            "        drop       1.00      1.00      1.00      2562\n",
            "  reset-both       1.00      0.67      0.80         6\n",
            "\n",
            "    accuracy                           1.00     13107\n",
            "   macro avg       1.00      0.92      0.95     13107\n",
            "weighted avg       1.00      1.00      1.00     13107\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print('Confusion Matrix:')\n",
        "print(confusion_matrix(y_test, y_pred))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "goKMkFoeAZs1",
        "outputId": "8cbcc0ac-be95-4a21-89db-dbaf98a764c6"
      },
      "execution_count": 45,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Confusion Matrix:\n",
            "[[7543    2    0    0]\n",
            " [   0 2987    7    0]\n",
            " [   0    9 2553    0]\n",
            " [   0    2    0    4]]\n"
          ]
        }
      ]
    }
  ]
}
