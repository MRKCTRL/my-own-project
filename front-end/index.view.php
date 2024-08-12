
    <div class="container">
      <div class="row">
        <div class="col-lg-12 text-center">
          <h1 class="mt-5"><?= $viewBag['heading'] ?></h1>
        </div>
      </div>
      <div class="row">
        <form class="for-inline" action="index.php" method="GET">
          <div class="form-group">
            <input type="text" name="search" id="search" value="">
            <input type="submit" name="" value="search">

          </div>
        </form>
      </div>
      <div class="row">
        <table class="table table-striped">
          <?php foreach ($model as $item ) : ?>
    <tr>
      <td> <a href="detail.php?term=<?= $item->id ?>" > <?= $item->term ?></a></td>
      <td><?= $item->definition ?></td>
    </tr>
  <?php endforeach;  ?>
  <?php if(true) : ?>
  <?php endif; ?>
        <!-- <?php
foreach ($model as $item ) {
  // code...
  $term = $item->term;
  $definition = $item->definition;
  echo "<tr><td>$term</td><td>$definition</td></tr";
}
         ?> -->
           </table>
      </div>
    </div>
