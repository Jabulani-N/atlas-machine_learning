# Transformer Applications

## Task 0

<details>
    <summary>instructions</summary>

Create the class `Dataset` that loads and preps a dataset for machine translation:


Class constructor `def __init__(self):`

creates the instance attributes:

* `data_train`, which contains the `ted_hrlr_translate/pt_to_en tf.data.Dataset train` split, loaded `as_supervided`

* `data_valid`, which contains the `ted_hrlr_translate/pt_to_en tf.data.Dataset validate` split, loaded `as_supervided`

* `tokenizer_pt` is the Portuguese tokenizer created from the training set

* `tokenizer_en` is the English tokenizer created from the training set

Create the instance method `def tokenize_dataset(self, data):` that creates sub-word tokenizers for our dataset:

* `data` is a `tf.data.Dataset` whose examples are formatted as a tuple `(pt, en)`

* `pt` is the `tf.Tensor` containing the Portuguese sentence

* `en` is the `tf.Tensor` containing the corresponding English sentence

* The maximum vocab size should be set to `2**15`

Returns: `tokenizer_pt`, `tokenizer_en`

* `tokenizer_pt` is the Portuguese tokenizer

* `tokenizer_en` is the English tokenizer

</details>

### Potential Pitfalls

Be sure the init method uses the `tokenize_dataset` method you just created in order to assign it's own tokenizers.

## Task 1

<details>
    <summary>summaryText</summary>
detailsText
</details>


<details>
    <summary>summaryText</summary>
detailsText
</details>


