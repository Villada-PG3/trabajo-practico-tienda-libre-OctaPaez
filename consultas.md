# Consultas
* 1
Producto.objects.all()
* 2
Categoria.objects.all()
* 3
Producto.objects.filter(precio__gt=15000)
* 4
Producto.objects.filter(nombre__icontains="pro")
* 5
Producto.objects.filter(stock__lt=10)
* 6
Producto.objects.exclude(activo=False)
* 7
Producto.objects.get(nombre="Shampoo Pantene")
* 8
Producto.objects.order_by("precio")

* 9
sp = Producto.objects.get(nombre="Shampoo Pantene")
sp.categoria

* 10 
capilar  = Categoria.objects.get(nombre="Capilar")
capilar.productos.all()

* 11
nueva_categoria = Categoria.objects.create(nombre='categoria prueba', slug='categoria_prueba')
Categoria.objects.get(nombre='categoria prueba')

# Resultados en consola
* 1
<QuerySet [<Producto: Acondicionador Dove - Dove - $8000.00 - Stock: 100>, <Producto: Acondicionador TRESemmé anti frizz - TRESemmé - $9000.00 - Stock: 100>, <Producto: Aquaphor Eucerin - Eucerin - $14000.00 - Stock: 30>, <Producto: Centella Protector Solar - Centella - $40000.00 - Stock: 3>, <Producto: Dermaglós Protector Solar - Dermaglós - $9000.00 - Stock: 20>, <Producto: HIdratante de manos Neutrógena - Neutrógena - $13000.00 - Stock: 10>, <Producto: HIdratante de manos cerave - Cerave - $14000.00 - Stock: 10>, <Producto: Hidratante Labial Burts Bees - Burts Bees - $15000.00 - Stock: 20>, <Producto: Hidratante Labial ISDIN - ISDIN - $13000.00 - Stock: 30>, <Producto: Hidratante Labial Nivea - Nivea - $5000.00 - Stock: 60>, <Producto: Hidratante de manos Caviahue - Caviahue - $12000.00 - Stock: 20>, <Producto: Hidratante de manos Dermaglos - Dermaglós - $1000.00 - Stock: 30>, <Producto: Hyalu B5 La Roche Possay - La Roche Possay - $40000.00 - Stock: 9>, <Producto: Life Activ VIchy - Vichy - $60000.00 - Stock: 5>, <Producto: Mela B3 La Roche Possay - La Roche Possay - $60000.00 - Stock: 5>, <Producto: Neutrogena Protector Solar Sun Fresh - Neutrógena - $14000.00 - Stock: 10>, <Producto: Retino B3 La Roche Possay - La Roche Possay - $80000.00 - Stock: 3>, <Producto: Shampoo Aveno - Aveno - $10000.00 - Stock: 40>, <Producto: Shampoo Pantene - Pantene - $7000.00 - Stock: 200>, <Producto: sunscreen fps50 - Nivea - $11000.00 - Stock: 23>]>

* 2
<QuerySet [<Categoria: Capilar>, <Categoria: Labios>, <Categoria: Manos>, <Categoria: Protectores Solares>, <Categoria: Rostro>, <Categoria: categoria_de_prueba>]>

* 3
<QuerySet [<Producto: Centella Protector Solar - Centella - $40000.00 - Stock: 3>, <Producto: Hyalu B5 La Roche Possay - La Roche Possay - $40000.00 - Stock: 9>, <Producto: Life Activ VIchy - Vichy - $60000.00 - Stock: 5>, <Producto: Mela B3 La Roche Possay - La Roche Possay - $60000.00 - Stock: 5>, <Producto: Retino B3 La Roche Possay - La Roche Possay - $80000.00 - Stock: 3>]>

* 4
<QuerySet [<Producto: Centella Protector Solar - Centella - $40000.00 - Stock: 3>, <Producto: Dermaglós Protector Solar - Dermaglós - $9000.00 - Stock: 20>, <Producto: Neutrogena Protector Solar Sun Fresh - Neutrógena - $14000.00 - Stock: 10>]>

* 5
<QuerySet [<Producto: Centella Protector Solar - Centella - $40000.00 - Stock: 3>, <Producto: Hyalu B5 La Roche Possay - La Roche Possay - $40000.00 - Stock: 9>, <Producto: Life Activ VIchy - Vichy - $60000.00 - Stock: 5>, <Producto: Mela B3 La Roche Possay - La Roche Possay - $60000.00 - Stock: 5>, <Producto: Retino B3 La Roche Possay - La Roche Possay - $80000.00 - Stock: 3>]>

* 6
<QuerySet [<Producto: Acondicionador Dove - Dove - $8000.00 - Stock: 100>, <Producto: Acondicionador TRESemmé anti frizz - TRESemmé - $9000.00 - Stock: 100>, <Producto: Aquaphor Eucerin - Eucerin - $14000.00 - Stock: 30>, <Producto: Centella Protector Solar - Centella - $40000.00 - Stock: 3>, <Producto: Dermaglós Protector Solar - Dermaglós - $9000.00 - Stock: 20>, <Producto: HIdratante de manos Neutrógena - Neutrógena - $13000.00 - Stock: 10>, <Producto: HIdratante de manos cerave - Cerave - $14000.00 - Stock: 10>, <Producto: Hidratante Labial Burts Bees - Burts Bees - $15000.00 - Stock: 20>, <Producto: Hidratante Labial ISDIN - ISDIN - $13000.00 - Stock: 30>, <Producto: Hidratante Labial Nivea - Nivea - $5000.00 - Stock: 60>, <Producto: Hidratante de manos Caviahue - Caviahue - $12000.00 - Stock: 20>, <Producto: Hidratante de manos Dermaglos - Dermaglós - $1000.00 - Stock: 30>, <Producto: Hyalu B5 La Roche Possay - La Roche Possay - $40000.00 - Stock: 9>, <Producto: Life Activ VIchy - Vichy - $60000.00 - Stock: 5>, <Producto: Mela B3 La Roche Possay - La Roche Possay - $60000.00 - Stock: 5>, <Producto: Neutrogena Protector Solar Sun Fresh - Neutrógena - $14000.00 - Stock: 10>, <Producto: Retino B3 La Roche Possay - La Roche Possay - $80000.00 - Stock: 3>, <Producto: Shampoo Aveno - Aveno - $10000.00 - Stock: 40>, <Producto: Shampoo Pantene - Pantene - $7000.00 - Stock: 200>, <Producto: sunscreen fps50 - Nivea - $11000.00 - Stock: 23>]>

* 7
<Producto: Shampoo Pantene - Pantene - $7000.00 - Stock: 200>

* 8
<QuerySet [<Producto: Hidratante de manos Dermaglos - Dermaglós - $1000.00 - Stock: 30>, <Producto: Hidratante Labial Nivea - Nivea - $5000.00 - Stock: 60>, <Producto: Shampoo Pantene - Pantene - $7000.00 - Stock: 200>, <Producto: Acondicionador Dove - Dove - $8000.00 - Stock: 100>, <Producto: Acondicionador TRESemmé anti frizz - TRESemmé - $9000.00 - Stock: 100>, <Producto: Dermaglós Protector Solar - Dermaglós - $9000.00 - Stock: 20>, <Producto: Shampoo Aveno - Aveno - $10000.00 - Stock: 40>, <Producto: sunscreen fps50 - Nivea - $11000.00 - Stock: 23>, <Producto: Hidratante de manos Caviahue - Caviahue - $12000.00 - Stock: 20>, <Producto: Hidratante Labial ISDIN - ISDIN - $13000.00 - Stock: 30>, <Producto: HIdratante de manos Neutrógena - Neutrógena - $13000.00 - Stock: 10>, <Producto: Aquaphor Eucerin - Eucerin - $14000.00 - Stock: 30>, <Producto: HIdratante de manos cerave - Cerave - $14000.00 - Stock: 10>, <Producto: Neutrogena Protector Solar Sun Fresh - Neutrógena - $14000.00 - Stock: 10>, <Producto: Hidratante Labial Burts Bees - Burts Bees - $15000.00 - Stock: 20>, <Producto: Hyalu B5 La Roche Possay - La Roche Possay - $40000.00 - Stock: 9>, <Producto: Centella Protector Solar - Centella - $40000.00 - Stock: 3>, <Producto: Mela B3 La Roche Possay - La Roche Possay - $60000.00 - Stock: 5>, <Producto: Life Activ VIchy - Vichy - $60000.00 - Stock: 5>, <Producto: Retino B3 La Roche Possay - La Roche Possay - $80000.00 - Stock: 3>]>

* 9
<Categoria: Capilar>

* 10
<QuerySet [<Producto: Acondicionador Dove - Dove - $8000.00 - Stock: 100>, <Producto: Acondicionador TRESemmé anti frizz - TRESemmé - $9000.00 - Stock: 100>, <Producto: Shampoo Aveno - Aveno - $10000.00 - Stock: 40>, <Producto: Shampoo Pantene - Pantene - $7000.00 - Stock: 200>]>

* 11
<Categoria: categoria prueba>