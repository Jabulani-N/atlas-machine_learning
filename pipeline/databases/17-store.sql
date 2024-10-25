-- creates a triggr for buying a given item
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW

    UPDATE items
    SET quantity = quantity - NEW.number
    WHERE items.name = NEW.item_name
;
