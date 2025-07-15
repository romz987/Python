SELECT 
    fv.name,
    fc.color,
    ft.type,
    fv.caloric
FROM fruits_and_vegetables fv 
JOIN fruit_color fc ON fv.color_id = fc.id
JOIN fruit_type ft ON fv.type_id = ft.id
;