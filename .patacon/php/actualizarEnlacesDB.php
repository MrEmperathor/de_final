#!/usr/bin/php
<?php
if ($argv[4] == "admin3") {
    $permiso = "admin3";
include 'conexion2.php';

}else{
    $permiso = "admin2";
    include 'conexion.php';
}
include 'funtions.php';

$id_db = $argv[1];
$link = $argv[2];
$datoBuscar = $argv[3];

switch ($datoBuscar) {
    case 'hqq.to':
        $dato = 'hqq.to';
        break;
    case 'jetload':
        $dato = 'jetload.net';
        break;
    case 'uptobox':
        $dato = 'uptobox.com';
        break;
    case 'gounlimited':
        $dato = 'gounlimited.to';
        break;
    case 'mega':
        $dato = 'mega.nz';
        break;
    case 'gdfree':
        $dato = 'drive.google.com/uc';
        break;
    case 'gdvip':
        $dato = 'drive.google.com/open';
        break;
    case 'short.pe':
        $dato = 'short.pe';
        break;
    case 'ouo.io':
        $dato = 'ouo.io';
        break;
    case 'formatearwindows.net':
            $dato = 'formatearwindows.net';
            break;
    default:
        echo "No existe dato a buscar";
        break;
}

if (!empty($link) && !empty($id_db)) {

    $sql_leer = "SELECT * FROM pelis WHERE id LIKE '%$id_db%' ORDER BY id";
    $gsent = $pdo->prepare($sql_leer);
    $gsent->execute();

    $resultado = $gsent->fetchAll();
    // var_dump($resultado);
    $array_enlaces = unserialize($resultado[0]['links']);
    // var_dump($array_enlaces);
    $validar = $array_enlaces[buscarDato($array_enlaces, $dato)];
    var_dump($validar);
    if (empty($validar)) {
        array_push($array_enlaces, $link);
    }else{
        $array_enlaces[buscarDato($array_enlaces, $dato)] = $link;
    }


    if (in_array($link, $array_enlaces)) {

        $seriaEnlaces = serialize($array_enlaces);

        $sql_editar = 'UPDATE pelis SET links=? WHERE id=?';
        $sentencia_editar = $pdo->prepare($sql_editar);
        $sentencia_editar->execute(array($seriaEnlaces,$id_db));

        //cerramos conexión base de datos y sentencia
        $pdo = null; 
        $sentencia_editar = null; 
    }else{
        echo "No se agrego el enlace";
    }
}


// var_dump($linkModificar);

// echo('<pre>');
// print_r($resultado);
// echo('</pre>');

// echo('<pre>');
// var_dump($array_enlaces);
// echo('</pre>');


?>
