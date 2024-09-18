(function () {
  const percentageSeen = (element) => {
    const parent = document.getElementById("stacked-cards-component-demo");
    const child = element.children.item(0);
    // Get the relevant measurements and positions
    const parentRect = parent.getBoundingClientRect();

    const childRect = child.getBoundingClientRect();

    if (childRect.bottom < parentRect.bottom) return 100;
    if (childRect.top > parentRect.bottom) return 0;
    return Math.round(
      (Math.abs(parentRect.bottom - childRect.top) / childRect.height) * 100
    );
  };
  const stackedCardsSection = document.getElementById(
    "stacked-cards-component-demo"
  );
  const stackedCards = document.getElementById("preview-stacked-cards");
  const cardsArray = Array.from(stackedCards.children);

  stackedCardsSection.addEventListener("scroll", function () {
    const percentageOfSecondCardSeen = percentageSeen(cardsArray[1]);
    const percentageOfThirdCardSeen = percentageSeen(cardsArray[2]);
    cardsArray[0].children.item(0).style.scale =
      1 -
      (0.1 * percentageOfSecondCardSeen) / 100 -
      (0.1 * percentageOfThirdCardSeen) / 100;
    cardsArray[0].children.item(0).style.opacity =
      1 -
      (0.1 * percentageOfSecondCardSeen) / 100 -
      (0.1 * percentageOfThirdCardSeen) / 100;
    cardsArray[0].children.item(0).style.filter = `blur(${
      (10 * percentageOfSecondCardSeen) / 100 +
      (10 * percentageOfThirdCardSeen) / 100
    }px)`;

    cardsArray[1].children.item(0).style.scale =
      1 - (0.1 * percentageOfThirdCardSeen) / 100;
    cardsArray[1].children.item(0).style.opacity =
      1 - (0.1 * percentageOfThirdCardSeen) / 100;
    cardsArray[1].children.item(0).style.filter = `blur(${
      (10 * percentageOfThirdCardSeen) / 100
    }px)`;
  });
})();
