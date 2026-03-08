<template>
  <aside class="column">
    <div class="description text-barlow">Matcher-Auswahl</div>

    <div id="port" class="port row justify-start"></div>
  </aside>
</template>

<style scoped>
aside {
  color: #fff;
  border-right: 1px solid #eee;
  padding: 10px;
  font-size: 16px;
  background: #10b981bf;
  -webkit-box-shadow: 0 5px 10px 0 rgba(0, 0, 0, 0.3);
  box-shadow: 0 5px 10px #0000004d;
  margin-bottom: 10px;
  max-height: 15vh;
}

aside .port > * {
  position: relative;
  margin-bottom: 10px;
  cursor: pointer;
  -webkit-box-shadow: 5px 5px 10px 2px rgba(0, 0, 0, 0.25);
  box-shadow: 5px 5px 10px 2px #00000040;
}

aside .description {
  margin-bottom: 10px;
}

@media screen and (min-width: 640px) {
  aside {
    min-width: 25%;
  }
}

@media screen and (max-width: 639px) {
  aside .port {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 5px;
  }
}
</style>
